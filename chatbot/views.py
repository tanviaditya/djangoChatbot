from django.shortcuts import render
from .apps import ChatbotConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd
import random
from chatbot.chat_file import chatbot
from googletrans import Translator
import http.client
import json
from time import sleep
from .models import Symptom

# Create your views here.
def translateText(text,src,dest):
    result=None
    translator = Translator()
    while result == None:
        try:
            result = translator.translate(text, src=src, dest=dest).text
        except Exception as e:
            # print(e)
            translator = Translator()
            sleep(0.5)
            pass
    return result      

class translate(APIView):
    def get(self,request):
        if request.method == 'GET':
            text = request.GET.get('text')
            lang=request.GET.get('lang')
            # translator = Translator()
            text=translateText(text,lang,'en')
            return JsonResponse({'text':text})

class call_model(APIView):

    def get(self,request):
        if request.method == 'GET':
            data = request.GET.get('data')
            lang=request.GET.get('lang')
            symp=chatbot.symptomDetector(data)
            # print(data)
            translator = Translator()
            # final_input=chatbot.inputNLP(symp)
            greetings=["Hi","hi","Hi there", "How are you ?", "Is anyone there?","Hola", "Hello", "Good day","Hey"]
            greetings_response=["Hello", "Good to see you again", "Hi, How can I help?"]
            exit_list=["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time","Thanks","Thank you","Gratitude"]
            exit_respose= ["See you!", "Have a nice day", "Bye!","Bye"]
            reply=""
            d=""
            p=""

            if data in greetings:
                reply=random.choice(greetings_response)
                if(lang!='en'):
                    reply=translateText(reply,'en',lang)
            elif data in exit_list:
                reply=random.choice(exit_respose)
                if(lang!='en'):
                    reply=translateText(reply,'en',lang)
            else:
                if len(symp)>0:
                    #add symptoms in database
                    for s in symp:
                            Symptom.objects.create(symptom=s)
                    symp_list = Symptom.objects.all()
                    if symp_list.count()<4: #length of symptoms in database
                        reply="Please enter few more symptoms"
                        if(lang!='en'):
                            reply=translateText(reply,'en',lang)
                    else:
                        #derive symptoms from database
                        symp_list = Symptom.objects.all().values('symptom')
                        symp_list=list(symp_list)
                        for i,s in enumerate(symp_list):
                            symp_list[i]=symp_list[i].get('symptom')
                        print("Final symptom list",symp_list)
                        final_input=chatbot.inputNLP(symp_list)
                        predict=ChatbotConfig.pickled_model.predict([final_input])
                        reply="You maybe suffering from "+(predict[0])
                        #delete all
                        Symptom.objects.all().delete()
                        if(lang!='en'):
                            reply=translateText(reply,'en',lang)
                        d=chatbot.getDescription(predict[0])
                        print("Prediction ",predict)
                        print("Here ",d)
                        d=d['Description'].values[0].title()
                        if(lang!='en'):
                            d=translateText(d,'en',lang)
                        r=chatbot.getPrecautions(predict[0])
                        r1="1] "+r['Precaution_1'].values[0].title()
                        r2="2] "+r['Precaution_2'].values[0].title()
                        r3="3] "+r['Precaution_3'].values[0].title()
                        r4="4] "+r['Precaution_4'].values[0].title()
                        p=r1+'\n'+r2+'\n'+r3+'\n'+r4
                        if(lang!='en'):
                            p=translateText(p,'en',lang)
                else:
                    reply="Please enter symptoms you are facing"   
                    if(lang!='en'):
                        reply=translateText(reply,'en',lang)
            return JsonResponse({'data':reply,
                                'description':d,
                                'precautions':p
                                })