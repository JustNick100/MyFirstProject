from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.contrib.auth.models import Group

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.core.files.storage import FileSystemStorage

from django.views.generic import ListView, TemplateView

from .forms import ItemForm
from .models import *


# Create your views here.

@unauthenticated_user
def registerpage(request):
	form = UserCreationForm()
		
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + user)
			return redirect('loginpage')

	context = {'form': form}
	return render(request, 'myapp/registerpage.html', context)

@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or Password is Incorrect')


	context = {}
	return render(request, 'myapp/loginpage.html', context)

def logoutUser(request):
	logout(request)
	return redirect('loginpage')


@login_required(login_url='loginpage')
@allowed_users(allowed_users=['customer'])
def customerpage(request):
	items = Item.objects.all()
	return render(request, 'myapp/customerpage.html', {'items':items})



@login_required(login_url='loginpage')
@admin_only
def home(request):
	items = Item.objects.all()
	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ItemForm()
	return render(request, 'myapp/home.html', {'form': form, 'items':items})

def delete_Item(request, pk):
	if request.method == 'POST':
		item = Item.objects.get(pk=pk)
		item.delete()
	return redirect('home')

def shoppingcartpage(request):
	return render(request, 'myapp/shoppingcartpage.html')