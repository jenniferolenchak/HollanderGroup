from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email',]


class CashFlowForm(ModelForm):


	class Meta:
		model = CashFlow
		fields = ['name','date','amount', 'category', 'type', 'recurring', 'description',]
		exclude = ['user',]


# https://timmyomahony.com/blog/upload-and-validate-image-from-url-in-django
# Check if the url has a valid extension for the file
class IconURLForm(forms.Form):

	url = forms.URLField(widget=forms.TextInput())

	VALID_IMAGE_EXTENSIONS = [
		".jpg",
		".jpeg",
		".png",
		".gif",
	]

	def is_valid_image_url(self, valid_extensions=VALID_IMAGE_EXTENSIONS):
		temp_url = self.cleaned_data['url'].lower()

		for extension in valid_extensions:
			if temp_url.endswith(extension):
				return True

		return False
