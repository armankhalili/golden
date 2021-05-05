import pickle
path = "C:/Users/HAL_9000/Desktop/bianary.dat"
myDict = {
    "firtname" : "Bill", 
    "lastname" : "gates",
    "age" : "64",
    "carrier" : "CEO & founder",
    "company" : "Microsoft"
}

myfile = open (path, "wb+")

pickle.dump(myDict, myfile)

myfile.close()
content = open (path, "rb")

toPrint = pickle.load(content)
print(toPrint)
content.close()