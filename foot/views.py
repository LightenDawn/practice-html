from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "foot/index.html")

def mynavigation(request):
    return render(request, "foot/mynav.html")