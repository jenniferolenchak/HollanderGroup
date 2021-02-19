# test_urls.py



from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *


class testUrls(SimpleTestCase):
	
	def test_home_url_resolves(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_register_url_resolves(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func, register)