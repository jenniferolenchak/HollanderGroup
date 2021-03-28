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

	def test_logged_in_user_can_view_upcoming_payments_tab(self):
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

		upcomingpayments_url = self.live_server_url + reverse('upcomingpayments')

		self.browser.get(upcomingpayments_url)

		self.assertEquals(
			self.browser.current_url, 
			upcomingpayments_url
			)

	def test_logged_in_user_can_add_upcoming_payment(self):
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

		add_upcomingpayments_url = self.live_server_url + reverse('addnewpayment')

		self.browser.get(add_upcomingpayments_url)

		# Ensure all page elements are visible by scrolling
		self.browser.execute_script("window.scrollTo(0,10000)")

		self.assertEquals(
			self.browser.current_url, 
			add_upcomingpayments_url
			)

		name_element = self.browser.find_element_by_id("id_name").send_keys('Test')
		date_element = self.browser.find_element_by_id("id_date").send_keys('03/14/2021')
		amount_element = self.browser.find_element_by_id("id_amount").send_keys("500.00")
		description_element = self.browser.find_element_by_id("id_description").send_keys("Test")

		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		all_upcomingpayments_url = self.live_server_url + reverse('allpayments')

		self.browser.get(all_upcomingpayments_url)

		self.assertTrue("Test" in self.browser.page_source)
		self.assertTrue("$500" in self.browser.page_source)
