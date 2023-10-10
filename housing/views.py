from django.shortcuts import render
import requests, uuid, json
from .forms import * 
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def translate (request):
    translateform = TranslateTextsForm()
    context = {'translateform':translateform}

    if request.method == 'POST':

        translateform = TranslateTextsForm(request.POST)

    return render(request,'translate.html',context)


