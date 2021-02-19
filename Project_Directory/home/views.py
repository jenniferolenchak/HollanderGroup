from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request, 'Home/index.html')
	# return HttpResponse	("Savester")

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			messages.success(request, f'Account created for {email}!')
			return redirect('Home/index.html')
	else:
		form = UserCreationForm()
	return render(request, 'Home/register.html', {'form': form})
