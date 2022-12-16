from Reference_table import models
from django import forms

class Form_for_Reference(forms.ModelForm):
    class Meta:
        model = models.Reference_table
        fields = "__all__"