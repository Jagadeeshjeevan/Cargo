
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
def home(request):
	return render(request, 'source/home.html')

def about(request):
	return render(request, 'source/about.html')

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				#login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('user/courier')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request,
				  template_name="source/login.html",
				  context={"form": form})


def courier_list(request):
	return render(request, 'user/list_user.html')


def user_track(request):
	return render(request, 'user/user_track.html')


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("home")