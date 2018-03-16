#
# M3TIOR 2018
#

# DJANGO
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db.models import Model
from django.db import models

# SYSTEM / STANDARD PYTHON
import io, os, sys
import importlib
import datetime
import decimal
import ctypes
import random
import string

# OPTIONAL
try:
	import lorem
except Error:
	lorem = None # Don't worry if we don't have lorem. Rand text is easy


# ALWAYS REPO NAME SINCE manage.py IS EXECUTED FROM THE ROOT
repository = os.path.abspath(os.path.dirname(sys.argv[0]))


def get_random_unicode(length):

	try:
		get_char = unichr
	except NameError:
		get_char = chr

	# Update this to include code point ranges to be sampled
	include_ranges = [
		( 0x0021, 0x0021 ),
		( 0x0023, 0x0026 ),
		( 0x0028, 0x007E ),
		( 0x00A1, 0x00AC ),
		( 0x00AE, 0x00FF ),
		( 0x0100, 0x017F ),
		( 0x0180, 0x024F ),
		( 0x2C60, 0x2C7F ),
		( 0x16A0, 0x16F0 ),
		( 0x0370, 0x0377 ),
		( 0x037A, 0x037E ),
		( 0x0384, 0x038A ),
		( 0x038C, 0x038C ),
	]

	alphabet = [
		get_char(code_point) for current_range in include_ranges
			for code_point in range(current_range[0], current_range[1] + 1)
	]
	return ''.join(random.choice(alphabet) for i in range(length))


class Command(BaseCommand):
	help = """
		An interface for quickly spawning database entries
	"""

	def _get_action_by_dest(self, parser, dest):
		for action in parser._get_optional_actions():
			if action.dest == dest:
				return action

	def add_arguments(self, parser):
		# Uses argparse.ArgumentParser()
		parser.add_argument(
			"APP",
			help="""
				the django app who's modules are being generated
			""",
			nargs = "?"
		)
		parser.add_argument(
			"MODEL",
			help="""
				the name of the django model which will be generated
			""",
			nargs = "?"
		)
		parser.add_argument(
			"-c", "--count",
			help="""
				the amount of models generated
			""",
			action = "store",
			type = int,
			metavar = "C"
		)
		parser.add_argument(
			"-b", "--blacklist",
			help="""
				when "attribute" is encountered, skip it
			""",
			nargs = "+",
			dest = "blacklist",
			metavar = "attribute"
		)
		parser.add_argument(
			"-a", "--auto",
			help="""
				specify automatic generation mode (this is all that is
				currently supported because lazy)
			""",
			action="store_const",
			const="auto",
			dest="mode"
		)
		parser.add_argument(
			"-l", "--lorem",
			help="""
				when automatic generation is enabled, toggles use of the
				lorem text engine for generating random text fields.
				(less robust testing; better looks)
			""",
			action="store_const",
			const = "lorem",
			dest = "stringtype"
		)
		parser.add_argument(
			"-u", "--unicode",
			help="""
				when automatic generation is enabled, toggles use of the
				UTF-8 for generating random text fields.
				(better testing, may cause instability)
			""",
			action="store_const",
			const = "unicode",
			dest = "stringtype"
		)


	def handle(self, *args, **options):
		# First we need to find whether or not
		app = os.path.join(repository,options["APP"])
		# The app we've decided to label is valid.
		if os.path.isdir(app):
			# Grab the module out of the working directory
			module = importlib.import_module(options["APP"]+".models")

			# Attempt to grab our desired model class
			model = getattr(module, options["MODEL"])
			for count in range(0,options["count"]):
				proto = model() 		# instanciate an empty copy of our model
										# so we can grab the model._meta value
										# and set our attribute values

				# The _meta.fields attribute holds all the declared values
				# local to the model we've defined, not Django's constructors.
				for field in proto._meta.fields:
					if field.name in options["blacklist"]:
						continue
					# XXX: THIS IS A HACK BE VERY ALERT;
					#	the usage of any variables beginning with an underscore
					#	as you probably know is dangerous because they're
					#	not a constant part of the API made public. So with
					#	updates to the Django framework, this is subject to
					#	change.
					#
					#		---The current Django vesion is (2.0)---
					#
					#		field.name	# the fields variable name
					#		field.model	# the fields model
					#
					if field.__class__ == models.AutoField or \
						field.__class__ == models.BigAutoField or \
						field.__class__ == models.FileField or \
						field.__class__ == models.ImageField or \
						field.__class__ == models.UUIDField or \
						field.__class__ == models.BinaryField:
						pass # DISREGARD

					#elif isinstance(field.model, models.BigIntergerField):
					#	setattr(proto, field.name, random.randint(0,2**64))

					elif field.__class__ == models.BooleanField or \
						field.__class__ == models.NullBooleanField:
						#-----------------------------------------------
						setattr(proto, field.name, bool(random.randint(0,1)))

					elif field.__class__ == models.CharField or \
						field.__class__ == models.EmailField or \
						field.__class__ == models.FilePathField or \
						field.__class__ == models.GenericIPAddressField or \
						field.__class__ == models.SlugField or \
						field.__class__ == models.URLField:
						#---------------------------------------
						if options["stringtype"] == "lorem" and lorem:
							text = lorem.text()[0: field.max_length]
							fixed = text[0:text.rfind(" ")]
							setattr(proto, field.name, fixed)
						elif options["stringtype"] == "unicode":
							out = ""
							for x in range(0, random.randint(0, max_length)):
								out = out + get_random_unicode()
							setattr(proto, field.name, out[0: field.max_length])
						else:
							# use ascii (middleground)
							out = ""
							for x in range(0, random.randint(0, 99999)):
								out = out + random.choice(string.printable)
							setattr(proto, field.name, out[0: field.max_length])


					elif field.__class__ == models.DateField:
						type=datetime.date

					elif field.__class__ == models.DateTimeField:
						type=datetime.datetime

					elif field.__class__ == models.DecimalField:
						setattr(
							proto,
							field.name,
							decimal.Decimal(
								float(random.randint(0,2**32)) + random.random()
							)
						)

					elif field.__class__ == models.DurationField:
						#---------------------------------------------
						type=datetime.timedelta

					elif field.__class__ == models.FloatField:
						setattr(
							proto,
							field.name,
							float(random.randint(0,2**32)) + random.random()
						)

					#elif isinstance(field.model, models.IntergerField) or \
					#	isinstance(field.model, models.PositiveIntegerField):
						#---------------------------------------------------
					#	setattr(proto, field.name, random.randint(0,2**32))

					#elif isinstance(field.model, models.PositiveSmallIntegerField) or \
					#	isinstance(field.model, models.SmallIntergerField):
						#-------------------------------------------------
					#	setattr(proto, field.name, random.randint(0,2**16))

					elif field.__class__ == models.TextField:
							if options["stringtype"] == "lorem" and TextLorem:
								text = lorem.text()
								setattr(proto, field.name, text)
							elif options["stringtype"] == "unicode":
								# DOESN'T FUNCTION PROPERLY YET
								out = ""
								for x in range(0, random.randint(0, 99999)):
									out = out + get_random_unicode()
								setattr(proto, field.name, out)
							else:
								# use ascii (middleground)
								out = ""
								for x in range(0, random.randint(0, 99999)):
									out = out + random.choice(string.printable)
								setattr(proto, field.name, out)

					elif field.__class__ == models.TimeField:
						type=datetime.time

					elif hasattr(field, "isrelation") and field.isrelation:
						relation = field.model # create empty instance
						choices = relation.get_choices() # DENOTE (returns array)
						choice = math.randint(1,len(choices))
						setattr(
							proto,
							field.name,
							relation.objects.get(id=int(choices[choice][0]))
						)
					else:
						continue # Don't handle error for now, too lazy
				print(proto)
				proto.save()
		else:
			print("error: couldn't find \""+app+"\"", io.stderr)
