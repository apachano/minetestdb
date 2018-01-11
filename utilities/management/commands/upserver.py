#
# M3TIOR 2018
#

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os
import sys

repository = os.path.abspath(os.path.dirname(sys.argv[0]))

class Command(BaseCommand):
	help = """
		automagically creates migrations for all project files,
		generates test data using the unittests and then runs runserver.
	"""

	def add_arguments(self, parser):
		# Uses argparse.ArgumentParser()
		parser.add_argument(
			"-V", "--global-verbosity",
			help="""
				sets the verbosity level for all django commands that
				upserver uses, including the verbosity level for this command
				itself.
			""",
			type=int, default=1
		)
		parser.add_argument(
			"--makemigrations-verbosity",
			help="sets the verbosity level for makemigrations",
			type=int, default=0
		)
		parser.add_argument(
			"--migrate-verbosity",
			help="sets the verbosity level for migrate",
			type=int, default=0
		)
		parser.add_argument(
			"--runserver-verbosity",
			help="sets the verbosity level for runserver",
			type=int, default=0
		)

	def handle(self, *args, **options):
		makemigrations_verbosity = (options['makemigrations_verbosity']
			if options['makemigrations_verbosity']
			else options['global_verbosity']
		)
		migrate_verbosity = (options['migrate_verbosity']
			if options['migrate_verbosity']
			else options['global_verbosity']
		)
		runserver_verbosity = (options['runserver_verbosity']
			if options['runserver_verbosity']
			else options['global_verbosity']
		)


		# Only getting surface apps for now because I'm uncertain
		# if we'll have any nested in the future.
		for root, dirnames, filnames in os.walk(repository):
			for dirname in dirnames:
				# exclude unix hidden files
				if ( dirname.find(".") == -1
					# blacklist any special cases
					and dirname != "management"
					and dirname != "templates"
					and dirname != "minetestdb"
				):
					call_command("makemigrations", dirname, verbosity=makemigrations_verbosity)
			break

		call_command("migrate", verbosity=migrate_verbosity)
		call_command("runserver", verbosity=runserver_verbosity)
