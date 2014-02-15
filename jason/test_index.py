from flask.ext.testing import TestCase, Twill
from bs4 import Beautifulsoup
from jason import app


class TestIndex(TestCase):
	""" Test idex """
	def create_app(self):
		app.config['TESTING'] = True
		return app

	def test_index(self):
		with Twill(self.app, port=5000) as t:
			t.browser.go(t.url('/'))