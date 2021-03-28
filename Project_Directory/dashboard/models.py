from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# This ensures our code will continue to work even if we change our default user model
User = get_user_model()

class Settings(models.Model):
	user = models.OneToOneField(User, related_name='settings', on_delete=models.CASCADE)

	# More Secure Phone number fields are possible to implement in the future
	phone_number = models.CharField(max_length=12, blank=True, null=True)
	location = models.CharField(max_length=140, blank=True, null=True)
	age = models.IntegerField(blank=True, null=True)
	student_status = models.BooleanField(blank=True, null=True)

	# If we have a means of storing static files, this will be a more valid method of storing images
	# icon = models.ImageField(upload_to='profile_image', blank=True)
	icon_url = models.URLField(blank=True, null=True)

	def __str__(self):
		return f"Profile Settings for {self.user.username}"


class BudgetList(models.Model):
	user = models.OneToOneField(User, related_name='budget', on_delete=models.CASCADE)

	# Set (null = True) so that fields are allowed to be blank
	balance = models.FloatField(default = 0.0)
	savings_goal = models.FloatField(default = 0.0)
	last_updated = models.DateField(auto_now = True, null = True)


class CashFlow(models.Model):
	# django doesn't naturally have a one to many field, so instead use the ForeignKey which
	# represents a Many to One. It points all of our cashflows to our budget
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

	# Name and date of cashflow
	name = models.CharField(max_length = 26, null = True)
	date = models.DateField(null = True)


	payment_choices = [("Payment", "Payment"), ("Income", "Income")]
	type = models.CharField(max_length = 26, choices = payment_choices, default = 'Payment', null = True)
	recurring_choices = ((True,"Yes"),(False,"No"))
	recurring = models.BooleanField(choices = recurring_choices, default = False, null = True)

	payment_categories = [("Housing", "Housing"), ("Utilities", "Utilities"), ("Transportation", "Transportation"), ("Food/Groceries", "Food/Groceries"), ("Shopping & Entertainment", "Shopping & Entertainemnt"), ("Subscriptions", "Subscriptions"), ("Health", "Health"), ("Savings Contribution", "Savings Contribution"), ("Other", "Other")]
	category = models.CharField(max_length = 26, choices = payment_categories, default = 'Food', null = True)
	# Currently assumes US dollars
	amount = models.FloatField(null = True)
	description = models.TextField(null = True)
	#category = models.CharField(max_length=140)
