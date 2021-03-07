from .forms import UserUpdateForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

@login_required(login_url="login")
def dashboard(request):
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
	return render(request, 'DashboardTemplates/upcomingpayments.html')