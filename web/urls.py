from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserView.as_view()),
    path('thank-you', views.thank_you)
]
