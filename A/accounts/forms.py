from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegister(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={"class": "form-control"}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("your email already exist")
        return email



