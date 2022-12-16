from django import forms
from . import models


class Form_for_bookshow(forms.ModelForm):
    class Meta:
        model = models.Staffing
        fields = "__all__"