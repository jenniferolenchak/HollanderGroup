from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# This ensures our code will continue to work even if we change our default user model
User = get_user_model()

class Settings(models.Model):
	user = models.OneToOneField(User, related_name='settings', on_delete=models.CASCADE)
	
	email = models.CharField(max_length=140)
	# More Secure Phone number fields are possible to implement in the future
	phone_number = models.CharField(max_length=12)
	location = models.CharField(max_length=140)
	age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
	student_status = models.BooleanField()

	def __str__(self):
		return f"Profile Settings for {self.user.username}"


class BudgetList(models.Model):
	user = models.OneToOneField(User, related_name='budget', on_delete=models.CASCADE)

	balance = models.IntegerField()
	savings_goal = models.IntegerField()
	last_updated = models.DateField()


class CashFlow(models.Model):
	# django doesn't naturally have a one to many field, so instead use the ForeignKey which 
	# represents a Many to One. It points all of our cashflows to our budget
	budget_list = models.ForeignKey(BudgetList, on_delete=models.CASCADE)

	date = models.DateField()

	# Check whether this is an expense or income
	is_cash_in_flow = models.BooleanField()
	is_cash_out_flow = models.BooleanField()

	# Currently assumes US dollars
	amount = models.FloatField()

	category = models.CharField(max_length=140)