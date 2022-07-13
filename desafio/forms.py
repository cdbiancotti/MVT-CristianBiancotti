from django import forms
from ckeditor.fields import RichTextFormField

class FormPerro(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    descripcion = RichTextFormField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaPerro(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)