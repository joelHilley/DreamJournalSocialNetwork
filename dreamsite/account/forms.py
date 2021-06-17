from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django_countries.fields import CountryField

class RegisterForm(UserCreationForm):
    class meta:
      model=Account
      email = forms.EmailField(max_length=255)
      date_of_birth = forms.DateField(help_text='YYYY-MM-DD')
      sex = forms.ChoiceField(choices=Account.SEX_CHOICES, required=False, help_text="Not Required")
      nationality = CountryField()

    class Meta:
        model = Account
        fields = ["email", "username", "date_of_birth", "sex", "nationality", "password1", "password2"]
