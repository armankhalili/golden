car_dict = {
    "brand" : "benz",
    "model" : "class30",
    "year" : 2021
}
print(car_dict,type(car_dict))
 
 ### change
car_dict["model"] = "class40" 

### get method
carModel = car_dict.get("model")
print(carModel)

### update

dic1 = {"brand" : " ford", "model" : "mustang" , "color" : "orange"}
car_dict.update(dic1)
print(car_dict)