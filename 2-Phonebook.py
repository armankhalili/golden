## library
import os
import time
Desktop_path= "C:/Users/HAL_9000/Desktop" ## 👈👈👈 enter you Desktop path
path = Desktop_path + "/db.txt"
## fuctions 
def addNumber(neme, number):
    f = open(path, "a+")
    newPhone = name + " : " + number + "\n"
    f.write(newPhone)
    f.close
def search(name) :  
    f = open(path, "r")
    for line in  f.readlines() :
        if name == line.split(" : ")[0] :
            print(name + " : " + line.split(" : ")[1])
    f.close()        
def delete(name) :
    f = open(path, "r")
    new_databse = ""
    for line in f.readlines():
        if not name == line.split(" : ")[0] :
            new_databse += line
    f.close()

    f = open(path,"w")
    f.write(new_databse)        
    
def showAll() :
    content = open(path, "r")
    print(content.read())
    content.close()
    

## validation
def validation():
     if not os.path.exists(path) :
        f = open(path, "w+")
        f.write("")
##  The main body of the software
ch = 1
while ch != 0 :
    os.system('cls')
    print("1-Add User\n2-Search Phone\n3-Delete User\n4-Show All Users\n0-Exit")
    ch=int(input("\nPlease Enter a number : "))
    os.system('cls')
    if ch == 1 :
        validation()
        name = input("\nEnter a name : ")
        os.system('cls')
        number = input("\nEnter number : ")
        os.system('cls')
        addNumber(name,number)
        os.system('cls')
        print("add user sucessfully !!!")
        time.sleep(2)
    elif ch == 2 :
        validation()
        name = input("\nEnter a name to search in phonebook : ")
        os.system('cls')
        search(name)
        input("\nPress Enter to get back in menu !!!")
    elif ch == 3 :
        validation()
        name = input("\nEnter a name to delete : ")
        os.system('cls')
        delete(name)
        os.system('cls')
        print("user has been deleted !!!")
        time.sleep(2)
    elif ch == 4 :
        showAll()
        input("\nPress Enter to get back in menu !!!")