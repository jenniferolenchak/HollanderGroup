# test_urls.py



from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import *


class testUrls(SimpleTestCase):
	
	def test_dashboard_url_resolves(self):
		url = reverse('dashboard')
		self.assertEquals(resolve(url).func, dashboard)

	def test_settings_url_resolves(self):
		url = reverse('settings')
		self.assertEquals(resolve(url).func, settings)

	def test_saving_suggestions_url_resolves(self):
		url = reverse('savingsuggestions')
		self.assertEquals(resolve(url).func, saving_suggestions)

	def test_upcoming_payments_url_resolves(self):
		url = reverse('upcomingpayments')
		self.assertEquals(resolve(url).func, upcoming_payments)