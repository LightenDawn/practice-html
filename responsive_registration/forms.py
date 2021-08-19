from django import forms
from django.forms import widgets
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"
        labels = {
            "full_name": "Your Name",
            "user_name": "Your Nickname",
            "email_address": "Your Email Address",
            "phone_number": "Your Phone Number",
            "password": "Your password",
            "confirm_password": "Your Password again",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty.",
                "max_length": "Please enter a shorter name!"
            },
            "phone_number": {
                "required" : "Your phone number can not be empty."
            },
            "password": {
                "required" : "Your password should not be empty."
            },
            "confirm_password": {
                "required" : "Your password should not be empty."
            }
        }
        widgets = {
            'full_name': forms.TextInput({"placeholder": "Enter your full name."}),
            'user_name': forms.TextInput({"placeholder": "Enter your user name."}),
            'email_address': forms.TextInput({"placeholder": "Enter your email address."}),
            'phone_number': forms.TextInput({"placeholder": "Enter your phone number."}),
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
            'gender': forms.RadioSelect()
        }