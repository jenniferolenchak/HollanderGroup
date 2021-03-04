from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import *

# Create your views here.

@login_required(login_url="login")
def dashboard(request):
	if request.method == 'POST':
		budgetInput = request.POST.get('budgetInput')
		
		request.user.budget.balance = budgetInput
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