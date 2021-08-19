from django.db import models
from django.db.models.fields import EmailField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserInfo(models.Model):
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email_address = EmailField()
    phone_number = PhoneNumberField(blank=False, unique=True, null=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    male = "ML"
    female = "FML"
    unknown = "UNK"
    GENDER_CHOICES = [
        (male, "ML"),
        (female, "FML"),
        (unknown, "UNK"),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=unknown)