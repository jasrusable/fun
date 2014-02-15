from flask.ext.testing import TestCase, Twill
from bs4 import Beautifulsoupo
from jason import app


class TestIndex(TestCase):
	""" Test idex """
	def create_app(self):
		app.config['TESTING'] = True
		return app