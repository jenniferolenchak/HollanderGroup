from .forms import *
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from .models import *
from datetime import datetime, timedelta
import random
from .utilities import *

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

	# All Required Information for the Charts
	user = request.user
	flows = CashFlow.objects.filter(user=user)

	payments_last_7_days = get_payments_total(user, d = 7)
	payments_last_30_days = get_payments_total(user, d = 30)
	payments_last_365_days = get_payments_total(user, d = 365)
	upcoming_payments_7_days = get_upcoming_payments_total(user, d = 7)
	upcoming_payments_30_days = get_upcoming_payments_total(user, d = 30)
	upcoming_income_30_days = get_upcoming_income_total(user, d = 30)
	upcoming_payments = get_upcoming_payments(user, d = 30)
	housing_payments = get_payments_in_category(user, d = 30, category = 'Housing')
	utilities_payments = get_payments_in_category(user, d = 30, category = "Utilities")
	transportation_payments = get_payments_in_category(user, d = 30, category = 'Transportation')
	food_payments = get_payments_in_category(user, d = 30, category = 'Food/Groceries')
	shopping_payments = get_payments_in_category(user, d = 30, category = 'Shopping & Entertainment')
	subscriptions_payments = get_payments_in_category(user, d = 30, category = 'Subscriptions')
	health_payments = get_payments_in_category(user, d = 30, category = 'Health')
	savings_payments = get_payments_in_category(user, d = 30, category = 'Savings Contribution')
	other_payments = get_payments_in_category(user, d = 30, category = 'Other')

	context = {'flows':flows,
				'payments_last_7_days' : payments_last_7_days,
				'payments_last_30_days' : payments_last_30_days,
				'payments_last_365_days' : payments_last_365_days,
				'upcoming_payments_7_days' : upcoming_payments_7_days,
				'upcoming_payments_30_days' : upcoming_payments_30_days,
				'upcoming_income_30_days' : upcoming_income_30_days,
				'upcoming_payments' : upcoming_payments,
				'housing_payments' : housing_payments,
				'utilities_payments' : utilities_payments,
				'transportation_payments' : transportation_payments,
				'food_payments' : food_payments,
				'shopping_payments' : shopping_payments,
				'subscriptions_payments' : subscriptions_payments,
				'health_payments' : health_payments,
				'savings_payments' : savings_payments,
				'other_payments' : other_payments,}

	return render(request, 'DashboardTemplates/dashboard.html', context=context)



@login_required(login_url='login')
def settings(request):
	return render(request, 'DashboardTemplates/settings.html')

@login_required(login_url='login')
def edit_accountinfo(request):

	# Form for editing user account info
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

	# Form for user personal info upload
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

	general_coupons = ['<a href="https://www.homedepot.com/c/coupons">General Deals: Check out Home Depot\'s Coupon Page</a>',
					   '<a href="https://www.bk.com/offers">General Deals: Check out Burger King Offers</a>',
					   '<a href="https://www.costco.com/join-costco.html">General Deals: Look into Receiving a Costco WholeSale Membership $60 or $120 Annual Membership</a>',
					   '<a href="https://www.walgreens.com/offers/offers.jsp">General Deals: See Walgreens Paperless Coupons</a>',
					   '<a href="https://www.publix.com/savings/digital-coupons">General Deals: See Publix Weekly Digital Coupons</a>',
					   '<a href="https://www.hulu.com/live-tv">General Deals: Hulu Plus Live TV $64/month</a>',
					   ]
	savings_strings += general_coupons

	if request.user.settings.student_status != None and request.user.settings.student_status == True:
		student_savings = ['<a href="https://www.spotify.com/us/student/">Spotify Premium Student (with Hulu and ShowTime) $4.99/month</a>',
						   '<a href="https://www.amazon.com/Amazon-Student/b?ie=UTF8&node=668781011">Amazon Prime Student First 6 Months Free</a>',
						   '<a href="https://www.audible.com/ep/students">Audible Get 3 Titles Every Month for just $9.95/month</a>',
						   '<a href="https://www.apple.com/apple-music/#:~:text=(1)%20Students%20can%20choose%20the,a%20three%2Dmonth%20free%20trial.">Apple Music for $4.99/month (regular price $9.99/month)</a>',
						   '<a href="https://www.nytimes.com/subscription/education/student?campaignId=6JQ7F">New York Times 4 week basic subscription free</a>',
						   '<a href="https://www.lenovo.com/us/en/landingpage/students-and-teachers/">Lenonvo Extra 5 % Off Sitewide</a>',
						   '<a href="https://www.microsoft.com/en-us/store/b/education">Microsoft Browse Student Deals</a>',
						   '<a href="https://www.myunidays.com/US/en-US">UNiDAYS deals website for students</a>',
						   '<a href="https://www.adobe.com/creativecloud/buy/students.html">Adobe Creative Cloud $19.99/month</a>',
						   '<a href="https://www.ableton.com/en/shop/education/">Ableton Live save 40 % on Music Production Software</a>',
						   '<a href="https://www.hulu.com/student">Hulu Student Subscription $1.99/month'
						    ]
		savings_strings += student_savings

	if request.user.settings.age != None and request.user.settings.age >= 13 and request.user.settings.age < 21:
		thirteen_or_older_savings = ['<a href="https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/apply-for-a-student-developer-pack"> \
									  Github any students over 13 eligible for Student Developer Pack</a>',
									]
		savings_strings += thirteen_or_older_savings

	if request.user.settings.age != None and request.user.settings.age >= 50:
		senior_50_up_savings = ['<a href="https://www.carrabbas.com/aarp">Carrabba\'s Italian Grill: 10% Off Entire Meal for AARP Members</a>',
								'<a href="https://www.seniordiscounts.com/FeaturedDiscounts/ChicfilA.aspx#:~:text=Discount%3A,purchase%20or%20a%2010%25%20discount.">\
								  	Chick-fil-A Senior Discount: Free refillable senior drink</a>',
								'<a href="https://www.walgreens.com/topic/promotion/seniorday.jsp">Walgreens Senior Day with AARP or Over 65</a>',
								'<a href="https://www.nps.gov/planyourvisit/passes.htm">National Parks Senior Lifetime Pass: $80 for access to over 2,000 sites</a>',
								'<a href="https://www.aarp.org/benefits-discounts/all/dennys-10003/">Denny\'s AARP 15% Off Your Check</a>'
								'<a href="https://www.aarp.org/benefits-discounts/all/bonefish-grill-10137/">Bonefish Grill 10% off AARP Members</a>',
								'<a href="https://www.att.com/offers/discount-program/aarp/">AA&T AARP Members Save $10/month on Wireless Plan</a>',
							  	]
		savings_strings += 	senior_50_up_savings

	if request.user.settings.age != None and request.user.settings.age >= 60:
		senior_60_up_savings = ['<a href="https://cs.kohls.com/app/answers/detail/a_id/101/~/age-specific-discounts#:~:text=We%20offer%20a%20special%2015,your%20age%20for%20this%20offer."> \
									Kohls Get 15% Off Every Wednesday for Seniors 60 or Older',
								]
		savings_strings += senior_60_up_savings

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

	# Gets a users payments or incomes
	user = request.user
	flows = CashFlow.objects.filter(user=user).order_by("date")

	# Separates user data based on time deltas
	payments_last_7_days = get_payments_total(user, d = 7)
	payments_last_30_days = get_payments_total(user, d = 30)
	payments_last_365_days = get_payments_total(user, d = 365)
	upcoming_payments_7_days = get_upcoming_payments_total(user, d = 7)
	upcoming_payments_30_days = get_upcoming_payments_total(user, d = 30)
	upcoming_income_30_days = get_upcoming_income_total(user, d = 30)
	upcoming_payments = get_upcoming_payments(user, d = 30).order_by("date")

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

	# Gets all payments or incomes for a user
	user = request.user
	flows = CashFlow.objects.filter(user=user).order_by("date")

	# Context for displaying info on html template
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

	# Gets flow to be removed
	flow = get_object_or_404(CashFlow, id=id)
	if request.method == "POST":
		flow.delete()
		return redirect('upcomingpayments')
	context = {"flow" : flow}
	return render(request, 'DashboardTemplates/delete.html', context)

@login_required(login_url='login')
def edit_cashflow(request, id):

	# Gets flow to be edited
	flow = get_object_or_404(CashFlow, id=id)

	if request.method == "POST":
		form = CashFlowForm(request.POST, instance=flow)
		if form.is_valid():
			form.save()

			return redirect('upcomingpayments')
	else:
		form = CashFlowForm(instance=flow)

	# Context for display on html template
	context = {"flow" : flow,
			   "form" : form}

	return render(request, 'DashboardTemplates/edit_cashflow.html', context)

@login_required(login_url='login')
def edit_icon_url(request):


	if request.method == 'POST':
		icon_form = IconURLForm(request.POST)

		if icon_form.is_valid():

			url = icon_form.cleaned_data.get("url")
			if icon_form.is_valid_image_url() and icon_form.image_exists():

				# Sets user icon as url
				request.user.settings.icon_url = url
				request.user.settings.save()

				messages.success(request, 'Your Account has been updated!')
				return redirect('settings')

			else:

				# If file extension is invalid, throw error message
				messages.error(request, 'Invalid File Extension or Link Found')
				icon_form = IconURLForm(request.POST)
	else:
		icon_form = IconURLForm(request.POST)

	context = {
		'icon_form': icon_form
	}

	return render(request, 'DashboardTemplates/edit_icon_url.html', context)
