from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def signup(request):
	return render(request, 'users/signup.html')

def register(request):
	user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect(reverse("users:profile"))
		else:
		# Return a 'disabled account' error message
			return HttpResponse("Disabled Account.")
	else:
		# Return an 'invalid login' error message.
		return HttpResponse("ERROR: Invalid Login")

def log_in(request):
	return render(request, 'users/log_in.html')

def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# http redirect
			return HttpResponseRedirect(reverse("users:profile"))
		else:
		# Return a 'disabled account' error message
			return HttpResponse("Disabled Account.")
	else:
		# Return an 'invalid login' error message.
		return HttpResponse("ERROR: Invalid Login")

def profile(request):
	if request.user.is_authenticated():
		user = request.user
		return render(request, 'users/profile.html', {'user':user})
		#return HttpResponse("You're logged in!")
	else:
		return render(request, 'users/login.html')

def logoutnow(request):
	logout(request)
	return HttpResponseRedirect(reverse("items:index"))


