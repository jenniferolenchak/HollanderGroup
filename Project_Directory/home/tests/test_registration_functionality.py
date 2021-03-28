# test_registration_functionality.py


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

	def test_registration_with_valid_user_redirects_to_login(self):

		self.browser.get(self.live_server_url + reverse('register'))

		# Ensure all page elements are visible by scrolling
		self.browser.execute_script("window.scrollTo(0,10000)")

		username_element = self.browser.find_element_by_id("id_username").send_keys('username')
		first_name_element = self.browser.find_element_by_id('id_first_name').send_keys('user')
		first_name_element = self.browser.find_element_by_id('id_last_name').send_keys('name')
		password_element = self.browser.find_element_by_id("id_email").send_keys('user@name.com')

		password_element = self.browser.find_element_by_id("id_password1").send_keys('wordpass1234!')
		password_element = self.browser.find_element_by_id("id_password2").send_keys('wordpass1234!')


		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		dashboard_url = self.live_server_url + reverse('login')
		
		self.assertEquals(
			self.browser.current_url,
			dashboard_url
			)

	def test_registration_with_common_password_is_not_permitted(self):

		self.browser.get(self.live_server_url + reverse('register'))

		self.browser.execute_script("window.scrollTo(0,10000)")

		username_element = self.browser.find_element_by_id("id_username").send_keys('username')
		first_name_element = self.browser.find_element_by_id('id_first_name').send_keys('user')
		first_name_element = self.browser.find_element_by_id('id_last_name').send_keys('name')
		password_element = self.browser.find_element_by_id("id_email").send_keys('user@name.com')

		password_element = self.browser.find_element_by_id("id_password1").send_keys('password')
		password_element = self.browser.find_element_by_id("id_password2").send_keys('password')

		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		dashboard_url = self.live_server_url + reverse('register')
		
		self.assertEquals(
			self.browser.current_url,
			dashboard_url
			)


	def test_registration_with_short_password_is_not_permitted(self):

		self.browser.get(self.live_server_url + reverse('register'))

		self.browser.execute_script("window.scrollTo(0,10000)")

		username_element = self.browser.find_element_by_id("id_username").send_keys('username')
		first_name_element = self.browser.find_element_by_id('id_first_name').send_keys('user')
		first_name_element = self.browser.find_element_by_id('id_last_name').send_keys('name')
		password_element = self.browser.find_element_by_id("id_email").send_keys('user@name.com')

		password_element = self.browser.find_element_by_id("id_password1").send_keys('1')
		password_element = self.browser.find_element_by_id("id_password2").send_keys('1')


		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		dashboard_url = self.live_server_url + reverse('register')
		
		self.assertEquals(
			self.browser.current_url,
			dashboard_url
			)

	def test_registration_with_unmatching_passwords_is_not_permitted(self):

		self.browser.get(self.live_server_url + reverse('register'))

		self.browser.execute_script("window.scrollTo(0,10000)")


		username_element = self.browser.find_element_by_id("id_username").send_keys('username')
		first_name_element = self.browser.find_element_by_id('id_first_name').send_keys('user')
		first_name_element = self.browser.find_element_by_id('id_last_name').send_keys('name')
		password_element = self.browser.find_element_by_id("id_email").send_keys('user@name.com')

		password_element = self.browser.find_element_by_id("id_password1").send_keys('1')
		password_element = self.browser.find_element_by_id("id_password2").send_keys('2')


		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		dashboard_url = self.live_server_url + reverse('register')
		
		self.assertEquals(
			self.browser.current_url,
			dashboard_url
			)