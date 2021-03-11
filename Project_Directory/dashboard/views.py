from .forms import UserUpdateForm, CashFlowForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from .models import *
from datetime import datetime

# Create your views here.

@login_required(login_url="login")
def dashboard(request):
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
	context = {'flows':flows}
	print(flows)
	return render(request, 'DashboardTemplates/upcomingpayments.html', context=context)


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
	
	flows = CashFlow.objects.all()
	print(flows)
	form = CashFlowForm()

	if request.method == 'POST':
		form = CashFlowForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			
		return redirect('upcomingpayments')

	context = {'flows':flows, 'form':form}
	return render(request,'DashboardTemplates/addnewpayment.html', context=context)