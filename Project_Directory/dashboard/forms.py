from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email',]


class CashFlowForm(ModelForm):

	class Meta:
		model = CashFlow
		fields = ['name','date','amount', 'type','description',]
		exclude = ['user',]