from google_trans_new import google_translator 
from time import sleep
text="I have fever"
result=None
translator = google_translator()
while result == None:
    try:
        result = translator.translate(text,lang_tgt='hi')
    except Exception as e:
        print(e)
        translator = Translator()
        sleep(0.5)
        pass      

print(result)


