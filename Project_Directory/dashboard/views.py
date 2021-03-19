from .forms import UserUpdateForm, CashFlowForm, IconURLForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from .models import *
from datetime import datetime, timedelta


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
def saving_suggestions(request):
	return render(request, 'DashboardTemplates/savingsuggestions.html')

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

	def get_upcoming_payments(user, d = 7):
		upcoming_d_days = datetime.now() + timedelta(days = d)
		payments = CashFlow.objects.filter(user = user, type = 'Payment', date__gt = datetime.now()).filter(date__lte = upcoming_d_days)
		
		return payments

	payments_last_7_days = get_payments_total(user, d = 7)
	payments_last_30_days = get_payments_total(user, d = 30)
	payments_last_365_days = get_payments_total(user, d = 365)
	upcoming_payments_7_days = get_upcoming_payments_total(user, d = 7)
	upcoming_payments = get_upcoming_payments(user, d = 30)

	context = {'flows':flows, 
				'payments_last_7_days' : payments_last_7_days, 
				'payments_last_30_days' : payments_last_30_days, 
				'payments_last_365_days' : payments_last_365_days,
				'upcoming_payments_7_days' : upcoming_payments_7_days,
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
def edit_icon_url(request):

	if request.method == 'POST':
		icon_form = IconURLForm(request.POST)
	
		if icon_form.is_valid():

			url = icon_form.cleaned_data.get("url").lower()

			if icon_form.is_valid_image_url():

				request.user.settings.icon_url = url
				request.user.settings.save()

				messages.success(request, 'Your Account has been updated!')
				return redirect('settings')

			else:
				messages.error(request, 'Invalid File Extension Found')
				icon_form = IconURLForm(request.POST)
	else:
		icon_form = IconURLForm(request.POST)

	context = {
		'icon_form': icon_form
	}

	return render(request, 'DashboardTemplates/edit_icon_url.html', context)