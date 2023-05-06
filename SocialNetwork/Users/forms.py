from django import forms
from .models import File

class xmlFile(forms.ModelForm):
    class Meta:
        model = File
        fields = ['archivo']

""" class Cargar(forms.Form):
    xml_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'})) """
    