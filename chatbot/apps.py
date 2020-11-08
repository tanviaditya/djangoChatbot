from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class ChatbotConfig(AppConfig):
    name = 'chatbot'
    path = os.path.join(settings.MODELS, 'FinalPickle.pkl')
    with open(path, 'rb') as pickled:
        pickled_model=pickle.load(pickled)
