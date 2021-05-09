import re
import requests

# variable 

url = "http://phpgeek.ir"
response = requests.get(url)
# print("response is :\n",response)

strSite = response.text

emailList = []

emailList = re.findall("[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+",strSite)
print("Email has been founded : ",emailList)