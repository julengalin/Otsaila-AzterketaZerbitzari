from django import forms
from .models import Jantzia, Diseinatzailea,Bilduma

class JantziaForm(forms.ModelForm):
    class Meta:
        model=Jantzia
        fields=['deskripzioa','kolorea','kopurua']

class DiseinatzaileaForm(forms.ModelForm):
    class Meta:
        model=Diseinatzailea
        fields=['izena','abizena','helbidea','emaila']

class BildumaForm(forms.ModelForm):
    class Meta:
        model=Bilduma
        fields=['jantzia','diseinatzailea']
    
    