from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages



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

