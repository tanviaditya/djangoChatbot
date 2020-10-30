from django.shortcuts import render
from .apps import ChatbotConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd
import random
from chatbot.chat_file import chatbot
from googletrans import Translator

# Create your views here.
class translate(APIView):
    def get(self,request):
        if request.method == 'GET':
            text = request.GET.get('text')
            translator = Translator()
            text=translator.translate(text, src='gu', dest='en').text
            return JsonResponse({'text':text})

class call_model(APIView):

    def get(self,request):
        if request.method == 'GET':
            data = request.GET.get('data')
            # lang=request.GET.get('lang')
            lang='gu'
            
            symp=chatbot.symptomDetector(data)
            print(data)
            translator = Translator()
            final_input=chatbot.inputNLP(symp)
            greetings=["Hi","hi","Hi there", "How are you ?", "Is anyone there?","Hola", "Hello", "Good day","Hey"]
            greetings_response=["Hello", "Good to see you again", "Hi, How can I help?"]
            exit_list=["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time","Thanks","Thank you"]
            exit_respose= ["See you!", "Have a nice day", "Bye!","Bye"]
            reply=""
            d=""
            p=""

            if data in greetings:
                reply=random.choice(greetings_response)
                if(lang!='en'):
                    reply=translator.translate(reply, src='en', dest=lang).text
            elif data in exit_list:
                reply=random.choice(exit_respose)
                if(lang!='en'):
                    reply=translator.translate(reply, src='en', dest=lang).text
            else:
                if len(symp)>0:
                    if len(symp)<3:
                        reply="Please enter few more symptoms"
                        if(lang!='en'):
                            reply=translator.translate(reply, src='en', dest=lang).text
                    else:
                        predict=ChatbotConfig.pickled_model.predict([final_input])
                        reply="You might have "+(predict[0])
                        if(lang!='en'):
                            reply=translator.translate(reply, src='en', dest=lang).text
                        d=chatbot.getDescription(predict[0])
                        d=d['Description'].values[0]
                        if(lang!='en'):
                            d=translator.translate(d, src='en', dest=lang).text
                        r=chatbot.getPrecautions(predict[0])
                        r1="1] "+r['Precaution_1'].values[0].title()
                        r2="2] "+r['Precaution_2'].values[0].title()
                        r3="3] "+r['Precaution_3'].values[0].title()
                        r4="4] "+r['Precaution_4'].values[0].title()
                        p=r1+'\n'+r2+'\n'+r3+'\n'+r4
                        if(lang!='en'):
                            p=translator.translate(p, src='en', dest=lang).text
                else:
                    reply="Please enter symptoms you are facing"   
                    if(lang!='en'):
                        reply=translator.translate(reply, src='en', dest=lang).text
            return JsonResponse({'data':reply,
                                'description':d,
                                'precautions':p
                                })
                