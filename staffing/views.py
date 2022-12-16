from django.shortcuts import render
from django.views import generic
from .models import Staffing
from .exel import read_file
from . import forms, models


class Staffing_table(generic.ListView):
    template_name = "staffing.html"
    df = read_file('file.xlsx')
    queryset = df
    success_url = ""



class StaffingCreatedateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.Form_for_bookshow
    queryset = models.Staffing.objects.all()
    success_url = "/home/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(StaffingCreatedateView, self).form_valid(form=form)