from django import forms

from .models import User_data

class UserForm(forms.ModelForm):
    class Meta:
        model = User_data
        fields = "__all__"

        labels = {
            "user_name": "Your Name",
            "email_address": "Your Email Address",
            "phone_number": "Your PhoneNumber",
            "rating": "Your Rating"
        }

        error_messages = {
            "user_name" : {
                "required": "You have to input your name!",
                "max_length": "You have to input the shorter name!"
            }
        }