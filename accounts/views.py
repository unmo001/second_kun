from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

from django.views import generic


class sighup(CreateView):
    form_class = 'signupform'
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login.html')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect('login.html')
