#
# M3TIOR 2018
#

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os
import sys
import shutil

# this winds up being our repo folder because this code is being
# executed from manage.py which is in the root of said folder.
repository = os.path.abspath(os.path.dirname(sys.argv[0]))

class Command(BaseCommand):
	help = """
		removes all prior migration data files.

		WARNING:
			this may cause instability in the SQL, use with caution
			in a product environment.
	"""

	def _get_action_by_dest(self, parser, dest):
		for action in parser._get_optional_actions():
			if action.dest == dest:
				return action

	def add_arguments(self, parser):
		# Uses argparse.ArgumentParser()
		pass

	def handle(self, *args, **options):
		verbosity = options['verbosity']
		# for each directory within the repository
		for root, dirnames, filenames in os.walk(repository):
			for dirname in dirnames:
				#find if migrations exist for the folder/app
				folder = os.path.join(repository, dirname, "migrations")
				if os.path.isdir(folder) and os.path.exists(folder):
					# then delete them all MUAHAHAHAHAHA!!!!
					shutil.rmtree(folder)
			break
