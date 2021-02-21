from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
	return render(request, 'Home/index.html')
	# return HttpResponse	("Savester")

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account was created')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'Home/register.html', {'form': form})
