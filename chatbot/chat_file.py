import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from googletrans import Translator
from django.conf import settings
import os

class chatbot:
    def getDescription(disease):
        path = os.path.join(settings.MODELS, 'symptom_Description.csv')
        dscp=pd.read_csv(path)
        r=dscp.loc[dscp['Disease']==disease]
        return r
    def getPrecautions(disease):
        path = os.path.join(settings.MODELS, 'symptom_precaution.csv')
        dscp=pd.read_csv(path)
        r=dscp.loc[dscp['Disease']==disease]
        return r
    def symptomDetector(text):
            tokens = word_tokenize(text.lower())
            words = [word for word in tokens if word.isalpha()]
            porter = PorterStemmer()
            stemmed = [porter.stem(word) for word in words]
            for s in stemmed:
                if s not in words:
                    words.append(s)
            final_symps=list()
            symptoms_dataset = pd.read_csv('E:\Fifth Semester\MP\healthcareChatBot\dataset\Symptoms.csv')
            symptoms_list= symptoms_dataset.Symptoms.tolist()
            # print("Symptoms",self.symptoms_list,len(self.symptoms_list))
            for symp in symptoms_list:
                s=""
                symp=s.join(symp)
                arr=symp.split("_")
                # print(arr,len(arr))
                for i,v in enumerate(arr):
                    arr[i]=v.strip()
                final_symps.append(arr)
            # print(final_symps,len(final_symps))
            symp=list()
            for i,w in enumerate(words):
                for j,s in enumerate(final_symps):
                    if(w==s[0]):
                        if len(s)>1:
                            word_index=i+1
                            c=0
                            for index,a in enumerate(s[1:]):
                                if s[index+1]==words[word_index]:
                                    word_index+=1
                                    c+=1
                            if c==len(s)-1:
                                z=w
                                for x in range(len(s)-1):
                                    z=z+"_"+words[i+x+1]
                                symp.append(z)
                        else:
                            symp.append(words[i])
            return(symp)

    def inputNLP(symp):
        symptoms_dataset = pd.read_csv('E:\Fifth Semester\MP\healthcareChatBot\dataset\Symptoms.csv')
        symptoms_dataset.columns=['Symptoms']
        symptoms_list= symptoms_dataset.Symptoms.tolist()        
        n=len(symptoms_list)
        final_input=[0 for i in range(n)]
        for s in symp:
            i=symptoms_list.index(s)
            final_input[i]=1
        return final_input
    
    def translateReply(text,lang):
        translator = Translator()
        if lang!='en' or lang!="":
            text=translator.translate(text, src='en', dest=lang).text
            return text
        else:
            return text