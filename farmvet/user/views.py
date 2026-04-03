from django.shortcuts import render, redirect

from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.views.generic import CreateView
#from django.views.generic import View

from django.contrib.auth import get_user_model, logout

from django.contrib.auth import login, authenticate
from .models import User, Vet_Officer, Farmer, Official,DairyCooperative
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import BasePermission   



User = get_user_model()

def vet0fficer_signup_view(request):
	if request.method == 'POST':
		form = forms.VetOfficerSignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_vet_officer = True
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.email = form.cleaned_data.get('email')
			user.phone_number = form.cleaned_data.get('phone_number')
			user.save()
			vet_officer = Vet_Officer.objects.create(user=user)
			vet_officer.kvb_number = form.cleaned_data.get('kvb_number')
			vet_officer.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}. You can now login')
			return redirect('vet-login')

	else:
		form = forms.VetOfficerSignUpForm()

	context = {
		'form':form
	}

	return render(request, 'user/vetregister.html', context)
	
def Official_signup_view(request):
	if request.method == 'POST':
		form = forms.OfficialSignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_official = True
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.email = form.cleaned_data.get('email')
			user.phone_number = form.cleaned_data.get('phone_number')
			user.save()
			official = Official.objects.create(user=user)
			official.employment_number = form.cleaned_data.get('employment_number')
			official.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}. You can now login')
			return redirect('official-login')

	else:
		form = forms.OfficialSignUpForm()

	context = {
		'form':form
	}

	return render(request, 'user/official.html', context)			


def farmer_signup_view(request):
	if request.method == 'POST':
		form = forms.FarmerSignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_farmer = True
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.email = form.cleaned_data.get('email')
			user.phone_number = form.cleaned_data.get('phone_number')
			user.save()
			farmer = Farmer.objects.create(user=user)
			farmer.farm_name = form.cleaned_data.get('farm_name')
			farmer.location = form.cleaned_data.get('location')
			farmer.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}. You can now login')
			return redirect('farmer-login')

	else:
		form = forms.FarmerSignUpForm()

	context = {
		'form':form
	}

	return render(request, 'user/farmerregister.html', context)

def cooperative_signup_view(request):
	if request.method == 'POST':
		form = forms.CooperativeSignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_cooperative = True
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.email = form.cleaned_data.get('email')
			user.phone_number = form.cleaned_data.get('phone_number')
			user.save()
			cooperative = DairyCooperative.objects.create(user=user)
			cooperative.cooperative_name = form.cleaned_data.get('cooperative_name')
			cooperative.sub_county = form.cleaned_data.get('sub_county')
			cooperative.location = form.cleaned_data.get('location')
			cooperative.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}. You can now login')
			return redirect('cooperative-login')

	else:
		form = forms.CooperativeSignUpForm()

	context = {
		'form':form
	}

	return render(request, 'user/cooperativereg.html', context)




		

def vet_login(request):
	form = AuthenticationForm()
	if request.method == 'POST':  
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			# Check if any user is already logged in, log them out first
			if request.user.is_authenticated:
				logout(request)
			
			if user.is_authenticated and user.is_vet_officer:
				login(request, user)
				return redirect('vet-portal')
			elif user.is_authenticated and user.is_farmer:
				messages.warning(request, 'Kindly login as a farmer')
				return redirect('farmer-login')
		else:
			messages.error(request, 'Invalid Credentials')

	return render(request, 'user/vetlogin.html', {'form': form})

def official_login(request):
	form = AuthenticationForm()
	if request.method == 'POST':  
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			# Check if any user is already logged in, log them out first
			if request.user.is_authenticated:
				logout(request)
			
			if user.is_authenticated and user.is_official:
				login(request, user)
				return redirect('official-portal')
			elif user.is_authenticated and user.is_farmer:
				messages.warning(request, 'Kindly login as a farmer')
				return redirect('farmer-login')

			elif user.is_authenticated and user.is_vet_officer:
				messages.warning(request, 'Kindly login as a veterinary  officer')
				return redirect('vet-login')
		else:
			messages.error(request, 'Invalid Credentials')

	return render(request, 'user/officiallogin.html', {'form': form})

def cooperative_login(request):
	form = AuthenticationForm()
	if request.method == 'POST':  
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			# Check if any user is already logged in, log them out first
			if request.user.is_authenticated:
				logout(request)
			
			if user.is_authenticated and user.is_cooperative:
				login(request, user)
				return redirect('cooperative-portal')
			elif user.is_authenticated and user.is_farmer:
				messages.warning(request, 'Kindly login as a farmer')
				return redirect('farmer-login')

			elif user.is_authenticated and user.is_vet_officer:
				messages.warning(request, 'Kindly login as a veterinary  officer')
				return redirect('vet-login')
			elif user.is_authenticated and user.is_official:
				messages.warning(request, 'Kindly login as a Government  official')
				return redirect('official-login')
		else:
			messages.error(request, 'Invalid Credentials')

	return render(request, 'user/cooperative.html', {'form': form})


def farmer_login(request):
	form = AuthenticationForm()
	if request.method == 'POST':  
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			# Check if any user is already logged in, log them out first
			if request.user.is_authenticated:
				logout(request)
			
			if user.is_authenticated and user.is_farmer:
				login(request, user)
				return redirect('farmer-portal')
			elif user.is_authenticated and user.is_vet_officer:
				messages.warning(request, 'Kindly login as a Vet Officer')
				return redirect('vet-login')
		else:
			messages.error(request, 'Invalid Credentials')

	return render(request, 'user/farmerlogin.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('index')