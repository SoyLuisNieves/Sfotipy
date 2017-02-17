from django.shortcuts import render
from django.contrib.auth import login

from .forms import UserCreationEmailForm, EmailAuthenticationForm

# Create your views here.

def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()
	return render(request, 'signup.html', {'form': form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)
	if form.is_valid():
		# loguear, login necesita 2 parametros: el request y el user, get_user es una funcion que esta dentro del formulario
		login(request, form.get_user())

	return render(request, 'signin.html', {'form': form})
