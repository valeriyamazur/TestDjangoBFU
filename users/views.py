from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.edit import CreateView

from users.forms import MyUserCreationForm

template = 'registration/signup.html'


def home(request):
    return render(request, "users/home.html")


class SignUp(View):

    def get(self, request):
        form = MyUserCreationForm
        context = {'form': form}
        return render(request, template, context)

    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            print(request.POST)
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                login(request, user)

                return redirect('home')

            else:
                messages.error(request, 'Something goes wrong!')
                messages.error(request, 'Password should contain at least one number without special symbols')
            context = {'form': form}
            return render(request, template, context)
