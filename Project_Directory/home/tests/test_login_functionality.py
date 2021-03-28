# test_login_functionality


from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from django.contrib.auth.models import User

# Note Currently Using ChromeWebDriver version 89
# ConnectionResetError may occur however they do not impact the validity of tests
class TestLoginPage(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Chrome('Home/tests/chromedriver.exe')

	def tearDown(self):
		self.browser.close()

	def test_login_with_valid_user_redirects_to_dashboard(self):
		user = User.objects.create_user('username', 'username@gmail.com', 'password')
		user.save()

		self.browser.get(self.live_server_url + reverse('login'))

		username_element = self.browser.find_element_by_id("username").send_keys('username')
		password_element = self.browser.find_element_by_id("password").send_keys('password')

		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		dashboard_url = self.live_server_url + reverse('dashboard')
		
		self.assertEquals(
			self.browser.current_url,
			dashboard_url
			)

	def test_login_with_invalid_user_does_not_redirect_to_dashboard(self):
		self.browser.get(self.live_server_url + reverse('login'))

		username_element = self.browser.find_element_by_id("username").send_keys('not_a_user')
		password_element = self.browser.find_element_by_id("password").send_keys('not_a_user')

		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		dashboard_url = self.live_server_url + reverse('login')
		
		self.assertEquals(
			self.browser.current_url,
			dashboard_url
			)

