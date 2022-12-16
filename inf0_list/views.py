from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import generic
from .models import Info_list

from . import forms, models


class Info_list_all(generic.ListView):
    template_name = "info_list.html"
    queryset = Info_list.objects.all()
    success_url = ""


class Info_listCreatedateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.Form_for_bookshow
    queryset = models.Info_list.objects.all()
    success_url = "/home/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Info_listCreatedateView, self).form_valid(form=form)