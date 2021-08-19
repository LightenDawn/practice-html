from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('cool', views.UserInputView.as_view())
]
