from django import forms
from . import models


class Form_for_bookshow(forms.ModelForm):
    class Meta:
        model = models.Info_list
        fields = "__all__"