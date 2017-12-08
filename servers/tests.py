from django.test import TestCase
from servers.models import Server

# Create your tests here.

class UI(TestCase):
	def setUp(self):
		s = []; # Server List
		s.push(Server(name="derp", version="1.2.3"))
		s.push(Server(name="thingy", version="2.3.3"))
		s.push(Server(name="floopbar", version="4.2.1"))
		for entry in s:
			entry.save()
