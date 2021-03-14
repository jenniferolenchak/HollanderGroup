# test_urls.py



from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *
from django.contrib.auth import views as auth_views


class testUrls(SimpleTestCase):
	
	def test_home_url_resolves(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_register_url_resolves(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func, register)

	def test_login_url_resolves(self):
		url = reverse('login')
		self.assertEquals(resolve(url).func, login_view)

	def test_logout_url_resolves(self):
		url = reverse('logout')
		self.assertEquals(resolve(url).func,logout_view)

	def test_password_reset_url_resolves(self):
		url = reverse('reset_password')
		self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)

	def test_password_reset_done_url_resolves(self):
		url = reverse('password_reset_done')
		self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

	def test_password_reset_complete_url_resolves(self):
		url = reverse('password_reset_complete')
		self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)