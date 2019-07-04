from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm


class Registration(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', context={'form': form})

    def post(self, request):
        bound_form = UserCreationForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()

            username = bound_form.cleaned_data['username']
            password = bound_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('tracks_list_url')
        return render(request, 'registration/register.html', context={'form': bound_form})


class Profile(View):
    def get(self):
        pass

    def post(self):
        pass