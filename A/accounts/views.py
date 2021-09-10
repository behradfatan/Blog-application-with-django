from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegister
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User



def user_login(request):
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('all_articles')
            else:
                messages.error(request, 'wrong username or password!!!', 'warning')
    else:
        forms = UserLoginForm()
    return render(request, 'user_login.html', {"forms": forms})


def user_register(request):
    if request.method == "POST":
        forms = UserRegister(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'successfully, go to login page', 'success')
            return redirect('user_login')
    else:
        forms = UserRegister()
        messages.error(request, 'some this is wrong', 'warning')
    return render(request, 'register.html', {"forms": forms})
