from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import UserForm
# Create your views here.

# class UserPageView(View):
#     def get(self, request):
#         return render(request, )

#     def post(self, request):


class UserView(View):
    def get(self, request):
        form = UserForm()

        return render(request, "web/first.html", {
            "form": form
        })

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        
        return render(request, "web/first.html", {
            "form": form
        })

def thank_you(request):
    return render(request, "web/thank_you.html", {
        "has_error": False
    })
