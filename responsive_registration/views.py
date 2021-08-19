from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView

from .models import UserInfo
from .forms import UserInfoForm
# Create your views here.

def index(request):
    return render(request, "responsive_registration/index.html")

class UserInputView(View):
    def get(self, request):
        form = UserInfoForm()

        return render(request, "responsive_registration/cool.html", {
            "form": form
        })
 
    def post(self, request):
        submitted_form = UserInfoForm(request.POST)

        if submitted_form.is_valid():
            submitted_form.save()
            return HttpResponseRedirect("/res/cool")
        
        return render(request, "responsive_registration/cool.html",{
            "form": submitted_form
        })

# class UserInputView(CreateView):
#     model = UserInfo
#     form_class = UserInfoForm
#     template_name = "responsive_registration/cool.html"
#     success_url = "/res/cool"