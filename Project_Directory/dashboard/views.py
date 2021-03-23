from .forms import UserUpdateForm, CashFlowForm, IconURLForm, PersonalInformationForm
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from .models import *
from datetime import datetime, timedelta
import random

# Create your views here.

@login_required(login_url="login")
def dashboard(request):

	# Create a settings object for users if possible
	request.user.settings, created_settings = Settings.objects.get_or_create(user = request.user)

	# Allow us to save our updated User Budget
	request.user.budget, created = BudgetList.objects.get_or_create(user = request.user)

	# If user doesn't already have a BudgetList, we declare and initialize one
	if created:
		request.user.budget.balance = 0
		request.user.budget.savings_goal = 0
		request.user.budget.last_updated = datetime.now()
		request.user.budget.save()

	return render(request, 'DashboardTemplates/dashboard.html')



@login_required(login_url='login')
def settings(request):
	return render(request, 'DashboardTemplates/settings.html')

@login_required(login_url='login')
def edit_accountinfo(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)

		if u_form.is_valid():
			u_form.save()
			messages.success(request, 'Your Account has been updated!')
			return redirect('settings')

	else:
		u_form = UserUpdateForm(instance=request.user)


	context = {
		'u_form': u_form
	}
	return render(request, 'DashboardTemplates/edit_accountinfo.html', context)

@login_required(login_url='login')
def personal_info(request):
	if (request.method == 'POST'):
		form = PersonalInformationForm(request.POST, instance=request.user.settings)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your personal information has been created')
			return redirect('settings')
	else:
		form = PersonalInformationForm(instance=request.user.settings)

	context = {
		'form': form
	}

	return render(request, 'DashboardTemplates/personal_info.html', context)

@login_required(login_url='login')
def saving_suggestions(request):

	# Get our settings so we can personalize suggestions
	request.user.settings, created_settings = Settings.objects.get_or_create(user = request.user)

	savings_strings = []

	if request.user.settings.student_status != None and request.user.settings.student_status == True:
		student_savings = ["Spotify Premium Student (with Hulu and ShowTime) $4.99/month", 
						   "Amazon Prime Student First 6 months free",
						   "Audible Get 1 free audiobook",
						   "Apple Music for $4.99/month (regular price $9.99/month)",
						   "New York Times 4 week basic subscription free",
						   "Lenonvo 5 % off",
						   "Microsoft 10 % off a new Surface Pro",
						   "UNiDAYS deals website for students",
						   "Adobe Creative Cloud $19.99/month",
						   "Ableton Live save 40 % on Music Production Software",
						    ]

		savings_strings += student_savings

	if request.user.settings.age != None and request.user.settings.age >= 13 and request.user.settings.age < 21:
		savings_string += "Github any students over 13 eligible for Student Developer Pack"

	if request.user.settings.age != None and request.user.settings.age >= 65:
		senior_savings = ["Applebee's Senior Discount: 10-15 % off",
						  "Arby's Senior Discount: 10 % off",
						  "Boston Market Senior Discount: Amount varies by location",
						  "Carrabba's Italian Grill: 10 % off entire meal for AARP members",
						  "Chick-fil-A Senior Discount: Free refillable senior drink",
						  "Dairy Queen Senior Discount: 10 % off ",
						  "Subway Senior Discount: 10 % off (varies by location",
						  "Bealls Senior Discount: 15 % off every Monday",
						  "National Parks Senior Lifetime Pass: $80 for access to over 2,000 sites"
						  ]
		savings_strings += senior_savings

	if request.method == "POST":
		pass

	else:
		# Select only up to 5 different savings to show the users
		random.shuffle(savings_strings)
		if len(savings_strings) > 5:
			savings_strings = savings_strings[:5]

	# If our savings strings is empty, we can't show any deals
	is_savings_strings_empty = False
	if len(savings_strings) == 0:
		is_savings_strings_empty = True

	context = {
		"is_savings_strings_empty" : is_savings_strings_empty,
		"savings_strings" : savings_strings
	}

	return render(request, 'DashboardTemplates/savingsuggestions.html', context)

@login_required(login_url='login')
def upcoming_payments(request):
	user = request.user
	flows = CashFlow.objects.filter(user=user)

	# Return total payments starting from d days ago to today
	def get_payments_total(user, d = 7):
		last_d_days = datetime.now() - timedelta(days = d)
		payments = CashFlow.objects.filter(user = user, type = 'Payment', date__gte = last_d_days).filter(date__lte = datetime.now())

		total = 0.0
		for payment in payments:
			total += payment.amount

		return total

	# Return all upcoming payments starting from tomorrow to d
	def get_upcoming_payments_total(user, d = 7):
		upcoming_d_days = datetime.now() + timedelta(days = d)
		payments = CashFlow.objects.filter(user = user, type = 'Payment', date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

		total = 0.0
		for payment in payments:
			total += payment.amount

		return total

	# Return all upcoming income starting from tomorrow to d
	def get_upcoming_income_total(user, d = 7):
		upcoming_d_days = datetime.now() + timedelta(days = d)
		payments = CashFlow.objects.filter(user = user, type = 'Income', date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

		total = 0.0
		for payment in payments:
			total += payment.amount

		return total

	def get_upcoming_payments(user, d = 7):
		upcoming_d_days = datetime.now() + timedelta(days = d)
		payments = CashFlow.objects.filter(user = user, date__gt = datetime.now()).filter(date__lte = upcoming_d_days)

		return payments

	payments_last_7_days = get_payments_total(user, d = 7)
	payments_last_30_days = get_payments_total(user, d = 30)
	payments_last_365_days = get_payments_total(user, d = 365)
	upcoming_payments_7_days = get_upcoming_payments_total(user, d = 7)
	upcoming_payments_30_days = get_upcoming_payments_total(user, d = 30)
	upcoming_income_30_days = get_upcoming_income_total(user, d = 30)
	upcoming_payments = get_upcoming_payments(user, d = 30)

	context = {'flows':flows,
				'payments_last_7_days' : payments_last_7_days,
				'payments_last_30_days' : payments_last_30_days,
				'payments_last_365_days' : payments_last_365_days,
				'upcoming_payments_7_days' : upcoming_payments_7_days,
				'upcoming_payments_30_days' : upcoming_payments_30_days,
				'upcoming_income_30_days' : upcoming_income_30_days,
				'upcoming_payments' : upcoming_payments}



	return render(request, 'DashboardTemplates/upcomingpayments.html', context=context)


@login_required(login_url='login')
def all_payments(request):
	user = request.user
	flows = CashFlow.objects.filter(user=user)


	context = {'flows':flows}



	return render(request, 'DashboardTemplates/allpayments.html', context=context)


@login_required(login_url='login')
def edit_my_data(request):

	if request.method == 'POST':
		# Allow us to save our updated User Budget
		request.user.budget, created = BudgetList.objects.get_or_create(user = request.user)

		# If user doesn't already have a BudgetList, we declare and initialize one
		if created:
			request.user.budget.balance = 0
			request.user.budget.savings_goal = 0
			request.user.budget.last_updated = datetime.now()
			request.user.budget.save()

		if request.POST.get('budgetButton'):
			budgetInput = request.POST.get('budgetInput')

			# Check if this is a valid float before storing
			if len(budgetInput) > 0 and  budgetInput.replace('.','',1).isdigit():
				request.user.budget.balance = budgetInput
				request.user.budget.last_updated = datetime.now()
				request.user.budget.save()

		elif request.POST.get('savingsGoalButton'):
			savingsGoalInput = request.POST.get('savingsGoalInput')

			# Check if this is a valid float before storing
			if len(savingsGoalInput) > 0 and savingsGoalInput.replace('.','',1).isdigit():
				request.user.budget.savings_goal = savingsGoalInput
				request.user.budget.last_updated = datetime.now()
				request.user.budget.save()

	return render(request, 'DashboardTemplates/editmydata.html')

@login_required(login_url='login')
def addnew_cashflow(request):

	# Creates payment object for 12 months
	def create_recurring(user, form):

		# Creates first month
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()

		# Creates following months
		for i in range(0,12):
			newform = form
			obj = newform.save(commit=False)
			obj.user = user
			obj.date = obj.date + timedelta(days = 30)
			obj.pk = None
			obj.save()



	flows = CashFlow.objects.filter(user=request.user)
	form = CashFlowForm()

	if request.method == 'POST':
		form = CashFlowForm(request.POST)
		if form.is_valid():
			recurring = form.cleaned_data['recurring']

			# If the payment is recurring, then create recurring payment objects
			if recurring == True:
				create_recurring(request.user, form)
			else:
				obj = form.save(commit=False)
				obj.user = request.user
				obj.save()

		return redirect('upcomingpayments')

	context = {'flows':flows, 'form':form}
	return render(request,'DashboardTemplates/addnewpayment.html', context=context)

@login_required(login_url='login')
def remove_cashflow(request, id):
	flow = get_object_or_404(CashFlow, id=id)
	if request.method == "POST":
		flow.delete()
		return redirect('upcomingpayments')
	context = {"flow" : flow}
	return render(request, 'DashboardTemplates/delete.html', context)


@login_required(login_url='login')
def edit_icon_url(request):

	if request.method == 'POST':
		icon_form = IconURLForm(request.POST)

		if icon_form.is_valid():

			url = icon_form.cleaned_data.get("url")
			if icon_form.is_valid_image_url() and icon_form.image_exists():

				request.user.settings.icon_url = url
				request.user.settings.save()

				messages.success(request, 'Your Account has been updated!')
				return redirect('settings')

			else:
				messages.error(request, 'Invalid File Extension or Link Found')
				icon_form = IconURLForm(request.POST)
	else:
		icon_form = IconURLForm(request.POST)

	context = {
		'icon_form': icon_form
	}

	return render(request, 'DashboardTemplates/edit_icon_url.html', context)
