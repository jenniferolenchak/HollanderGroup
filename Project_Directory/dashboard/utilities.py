# utilities.py
# Utility functions used by the views pages

from datetime import datetime, timedelta
from .models import *
from django.db import models

# Return value of total payments starting from d days ago to today
def get_payments_total(user, d = 7):
	last_d_days = datetime.now() - timedelta(days = d)
	payments = CashFlow.objects.filter(user = user, type = 'Payment', date__gte = last_d_days).filter(date__lte = datetime.now())

	total = 0.0
	for payment in payments:
		total += payment.amount

	return total

# Return value of all upcoming payments starting from tomorrow to d
def get_upcoming_payments_total(user, d = 7):
	upcoming_d_days = datetime.now() + timedelta(days = d)
	payments = CashFlow.objects.filter(user = user, type = 'Payment', date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

	total = 0.0
	for payment in payments:
		total += payment.amount

	return total

# Return value of all upcoming income starting from tomorrow to d
def get_upcoming_income_total(user, d = 7):
	upcoming_d_days = datetime.now() + timedelta(days = d)
	payments = CashFlow.objects.filter(user = user, type = 'Income', date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

	total = 0.0
	for payment in payments:
		total += payment.amount

	return total

# Returns list of all upcoming payments starting from tomorrow to d
def get_upcoming_payments(user, d = 7):
	upcoming_d_days = datetime.now() + timedelta(days = d)
	payments = CashFlow.objects.filter(user = user, date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

	return payments

# Returns value of cashflow payments in specific category, from tomorrow to d
def get_payments_in_category(user, d = 7, category = 'Housing'):
	upcoming_d_days = datetime.now() + timedelta(days = d)
	payments = CashFlow.objects.filter(user = user, type = 'Payment', category = category, date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

	total = 0.0
	for payment in payments:
		total += payment.amount

	return total
