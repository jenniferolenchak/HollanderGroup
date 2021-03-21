# test_views.py


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import json

class testViews(TestCase):

	# Create Logged In User to Test Views for Users
	def setUp(self):
		self.client = Client()
		self.client.force_login(User.objects.get_or_create(username='test')[0])

	def test_dashboard_view(self):
		url = reverse('dashboard')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'DashboardTemplates/dashboard.html')

	def test_settings_view(self):
		url = reverse('settings')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'DashboardTemplates/settings.html')

	def test_saving_suggestions_view(self):
		url = reverse('savingsuggestions')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'DashboardTemplates/savingsuggestions.html')

	def test_upcoming_payments_view(self):
		url = reverse('upcomingpayments')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'DashboardTemplates/upcomingpayments.html')

	def test_edit_my_daya_view(self):
		url = reverse('editmydata')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'DashboardTemplates/editmydata.html')	

	# The following tests require that the client be logged out
	def test_dashboard_redirects_anonymous_users_to_login_page(self):
		self.client.logout()

		url = reverse('dashboard')
		response = self.client.get(url)

		# 302 is redirect status code
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/login/?next=/dashboard/')

	def test_dashboard_redirects_anonymous_users_to_login_page(self):
		self.client.logout()

		url = reverse('dashboard')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/login/?next=/dashboard/')

	def test_settings_redirects_anonymous_users_to_login_page(self):
		self.client.logout()

		url = reverse('settings')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/login/?next=/dashboard/settings/')

	def test_saving_suggestions_redirects_anonymous_users_to_login_page(self):
		self.client.logout()

		url = reverse('savingsuggestions')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/login/?next=/dashboard/savingsuggestions/')


	def test_upcoming_payments_redirects_anonymous_users_to_login_page(self):
		self.client.logout()

		url = reverse('upcomingpayments')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/login/?next=/dashboard/upcomingpayments/')

