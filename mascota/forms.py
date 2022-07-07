
from django import forms

class BusquedaGato(forms.Form):
    apodo = forms.CharField(max_length=30, required=False)