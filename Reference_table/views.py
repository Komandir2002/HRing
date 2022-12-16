from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import generic

from .forms import Form_for_Reference
from .models import Employee,Department,Reference_table



class Reference_table_view(generic.ListView):
    template_name = "reference_list.html"
    queryset = Reference_table.objects.all()
    success_url = "/home/"




class ReferenceDetailView(generic.DetailView):
    template_name = "reference_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(Reference_table, id=show_id)


class ReferenceCreatedateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = Form_for_Reference
    queryset = Reference_table.objects.all()
    success_url = "/home/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ReferenceCreatedateView, self).form_valid(form=form)


class ReferenceUpdateView(generic.UpdateView):
    template_name = "reference_update.html"
    form_class = Form_for_Reference
    success_url = "/home/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(Reference_table, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ReferenceUpdateView, self).form_valid(form=form)


class ReferenceDeleteView(generic.DeleteView):
    success_url = "/home/"
    template_name = "confirm_delete_reference.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(Reference_table, id=show_id)