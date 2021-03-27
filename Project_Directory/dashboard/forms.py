from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
import requests

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email',]


class CashFlowForm(ModelForm):
	class Meta:
		model = CashFlow
		fields = ['name','date','amount', 'category', 'type', 'recurring', 'description',]
		exclude = ['user',]

class PersonalInformationForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['phone_number', 'location', 'age', 'student_status',]

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
		url_lowered = self.cleaned_data['url'].lower()

		for extension in valid_extensions:
			if url_lowered.endswith(extension):
				return True

		return False

	# Check to see if image exists on website
	# https://stackoverflow.com/questions/2486145/python-check-if-url-to-jpg-exists
	def image_exists(self):
		try:
			url = self.cleaned_data['url']
			request = requests.head(url)
		except:
			return False

		# Return if the connection was success or not
		return request.status_code in (200, 301, 302)
