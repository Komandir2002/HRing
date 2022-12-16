from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import generic

from . import forms, models
from .forms import RegisterationForm, LoginForm
from .models import Employee

class RegisterView(generic.CreateView):
    form_class = RegisterationForm
    template_name = "registation.html"
    success_url = "/bookshow/"


# Create your views here.


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = "/bookshow/"

    # def get_success_url(self):
    #     return self.success_url

    def get_redirect_url(self):
        return self.success_url


class UserListView(generic.ListView):
    template_name = "users.html"
    queryset = User.objects.all()


class Employes(generic.ListView):
    template_name = "employe_table.html"
    queryset = Employee.objects.all()
    success_url = "/employes/"


class EmployeDetailView(generic.DetailView):
    template_name = "employe_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Employee, id=show_id)


class EmployeCreatedateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.Form_for_Employe
    queryset = models.Employee.objects.all()
    success_url = "/home/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EmployeCreatedateView, self).form_valid(form=form)




class EmployeUpdateView(generic.UpdateView):
    template_name = "employe_update.html"
    form_class = forms.Form_for_Employe
    success_url = "/home/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Employee, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EmployeUpdateView, self).form_valid(form=form)


class EmployeDeleteView(generic.DeleteView):
    success_url = "/home/"
    template_name = "confirm_delete_employe.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Employee, id=show_id)