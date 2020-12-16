# import http.client
# import json
# # import jsonurl
# conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

# payload ={
#     "q":"Hello world",
#     "source":"en",
#     "target":"gu",
# }
# # payload=JSON.stringify(payload)
# # "q=Hello%2C%20world!&source=en&target=gu"
# # payload = jsonurl.query_string(payload)
# headers = {
#     'content-type': "application/x-www-form-urlencoded",
#     'accept-encoding': "application/gzip",
#     'x-rapidapi-key': "acceac1621msh846fafdf56d7872p1224d8jsn37b1f64ff23e",
#     'x-rapidapi-host': "google-translate1.p.rapidapi.com"
#     }

# conn.request("POST", "/language/translate/v2",payload,headers)

# res = conn.getresponse()

# data = res.read()

# print(data.decode("utf-8"))


# # import json

# # # a Python object (dict):
# # x = {
# #     "q":"Hello world",
# #     "source":"en",
# #     "target":"gu",
# # }

# # # convert into JSON:
# # y = json.dumps(x,separators=(',', ':'))
# # # json_mylist = json.dumps(mylist, separators=(',', ':'))

# # # the result is a JSON string:
# # print(y)

from googletrans import Translator
from time import sleep
text="I have fever"
result=None
translator = Translator()
while result == None:
    try:
        result = translator.translate(text, src='en', dest='hi').text
    except Exception as e:
        print(e)
        translator = Translator()
        sleep(0.5)
        pass      

print(result)


