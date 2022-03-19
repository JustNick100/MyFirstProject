from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Item

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('title', 'picture', 'height', 'width', 'manufacturingcountry', 'description', 'price')
