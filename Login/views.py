from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from Login.forms import LoginForm

class SpecificUserLoginView(LoginView):    
    form_class = LoginForm
    template_name = 'login.html'

def logoutView(request):
    logout(request)
    return redirect("login")