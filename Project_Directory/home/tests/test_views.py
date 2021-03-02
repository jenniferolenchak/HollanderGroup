# test_views.py



from django.test import TestCase, Client
from django.urls import reverse
import json
from django.contrib.auth.models import User


class testViews(TestCase):
	def setUp(self):
		self.client = Client()

	def test_home_view(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Home/index.html')

	def test_register_view(self):
		url = reverse('register')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Home/register.html')

	def test_login_view(self):
		url = reverse('login')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Home/login.html')

	def test_logout_view(self):
		url = reverse('logout')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 302)
	