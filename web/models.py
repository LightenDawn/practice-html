from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class User_data(models.Model):
    user_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = PhoneNumberField(blank=False, unique=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])