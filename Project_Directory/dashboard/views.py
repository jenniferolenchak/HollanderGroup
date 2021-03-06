from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import *
from datetime import datetime


# Create your views here.

@login_required(login_url="login")
def dashboard(request):
	if request.method == 'POST':
		budgetInput = request.POST.get('budgetInput')

		# Allow us to save our updated User Budget
		request.user.budget, created = BudgetList.objects.get_or_create(user = request.user)

		# If user doesn't already have a BudgetList, we initialize it
		if created:
			request.user.budget.balance = 0
			request.user.budget.savings_goal = 0
			request.user.budget.last_updated = datetime.now()
			
		else:
			request.user.budget.balance = budgetInput
			request.user.budget.last_updated = datetime.now()
			
		request.user.budget.save()


	return render(request, 'DashboardTemplates/dashboard.html')



@login_required(login_url='login')
def settings(request):
	return render(request, 'DashboardTemplates/settings.html')

@login_required(login_url='login')
def saving_suggestions(request):
	return render(request, 'DashboardTemplates/savingsuggestions.html')

@login_required(login_url='login')
def upcoming_payments(request):
	return render(request, 'DashboardTemplates/upcomingpayments.html')