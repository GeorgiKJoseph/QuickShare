from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('header','text')
    #attachment = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))