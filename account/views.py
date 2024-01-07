from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.


class UserRegisteration(View):
    def get(self, request):
        form = forms.UserRegisterationForm()
        return render(request, "account/register.html" , {"form": form})

    def post(self, request):
        pass
