from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserLoginForm


def user_login(request):
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
    else:
        forms = UserLoginForm()
    return render(request, 'user_login.html', {"forms": forms})

