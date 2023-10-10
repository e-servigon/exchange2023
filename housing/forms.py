from django import forms
from django.forms import Textarea 
from .models import *

class TranslateTextsForm(forms.ModelForm):
    class Meta:
        model = TranslateTexts
        fields = ['text_to_translate','language_code_destiny']