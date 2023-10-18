from django.shortcuts import render
import requests, uuid, json
from .forms import * 
from .models import *
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def translate (request):
    translateform = TranslateTextsForm()
    context = {'translateform':translateform}

    if request.method == 'POST':

        translateform = TranslateTextsForm(request.POST)
        #CODIGO DE API DE TRADUCCION
        key = "60d45efe64884f5eb4a1b3984f7173a9"
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "eastus"

        path = '/translate'
        constructed_url = endpoint + path
        print(constructed_url)

        #parametros del servicio de traducción, versión, idioma origen e idioma destino 
        from_language= 'es'
        to_language= request.POST.get('language_code_destiny')
        params = {
            'api-version': '3.0',
            'from': from_language,
            'to': [to_language]
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        #valor que tu mandas para que la API realice algo
        sentence = request.POST.get('text_to_translate')
        body = [{
            'text': sentence
        }]

        translate = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = translate.json()

        print(response[0].get('translations')[0].get("text"))
        context['responsetranslate']= response[0].get('translations')[0].get("text")
        new_row = TranslateTexts.objects.create(language_code_origin=from_language, language_code_destiny=to_language, text_to_translate=sentence, text_translated= response[0].get('translations')[0].get("text"))
        new_row.save()

    return render(request,'translate.html',context)

def sentiment (request):
    analyzeform = AnalyzeTextsForm()
    context = {'analyzeform':analyzeform}

    if request.method == 'POST':
        #datos que coloca el usuario
        analyzeform = AnalyzeTextsForm(request.POST)
        #API sentiment
        credential = AzureKeyCredential("fad32181f2334484892d89722c6d7761")
        endpoint = "https://lenguajedscrscl.cognitiveservices.azure.com/"

        text_analytics_client = TextAnalyticsClient(endpoint,credential)
        documents = [request.POST.get('text_to_analyze')]
        response = text_analytics_client.analyze_sentiment(documents,language="es") 

        result = [doc for doc in response if not doc.is_error] 
        print(result) 
        for doc in result:
            print("sentimiento general:",doc.sentiment)
            print("VALOR POSITIVO:",doc.confidence_scores.positive,"VALOR NEGATIVO:",doc.confidence_scores.negative,"VALOR NEUTRAL:",doc.confidence_scores.neutral)
            context['sentimentresult']=doc.sentiment
            new_row = SentimentTexts.objects.create(text_to_analyze=request.POST.get('text_to_analyze'), sentiment_result=doc.sentiment)
            new_row.save()

    return render(request,'sentiment.html',context)

