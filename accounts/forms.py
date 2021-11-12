from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Privacy, Address


class UserForm(UserCreationForm):
    code = forms.CharField(label="인증코드")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'code']


class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = ['name', 'birth', 'l_food1', 'l_food2', 'l_food3',
                  'h_food1', 'h_food2', 'h_food3', 'good', 'bad', 'hobby']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone', 'postal', 'addy']
