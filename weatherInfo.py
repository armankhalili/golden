import json,requests

cityID = "2251945"    # tehran woeid 
url = "https://www.metaweather.com/api/location/"+cityID+"/" 

response = requests.get(url)  # get response

weatherInfo = response.json() # convert to json formate

history = open("C:/Users/HAL_9000/Desktop/history.txt","a+") # open a file

json.dump(weatherInfo,history) # dump the json data

