#libraris
import pickle,time,os
path = "C:/Users/HAL_9000/Desktop/library-manager/"
#functions
def addUser(name,fname,fathername,Ncode,birthday) :
    filepath = path + "users.dat"
    file = open(filepath,"rb")
    userData = pickle.load(file)
    file.close()

    #creat user 
    userID = int(len(userData))
    userData[userID] = [name, fname, fathername, Ncode, birthday]

    #write user data to the file
    file = open(filepath, "wb")
    pickle.dump(userData,file)

def addBook(title, author, subject, year) :

    #read data from bianary file
    filepath = path + "books.dat"
    file = open(filepath,"rb")
    bookData = pickle.load(file)
    file.close
    
    #creat a book
    bookData[title] = [author, subject, year]

    # write information to bianary file 
    file = open(filepath, "wb")
    pickle.dump(bookData,file)
    file.close

def search(title) :

    # validation of existing file 
    checkFile("books.dat")

    #read data from bianary file
    filepath = path + "books.dat"
    file = open(filepath,"rb")
    bookData = pickle.load(file)
    file.close

    #print result of search
    try : 
        theBook = bookData[title]
        print("\n\nBook has been found :\nName : {}\nAuthor : {}\nSubject : {}\nPublish Year : {}".format(title,theBook[0],theBook[1],theBook[2]))
    except :
        print("Book not found")

def barrowBook(userid,title) :
    filepath = path + "barrow.dat"
    #read information and store to a variable
    file = open(filepath,"rb")
    barrowDict = pickle.load(file)
    file.close()

    barrowDict[userid] = title

    file = open(filepath, "wb")
    pickle.dump(barrowDict,file)

    print( "{} has been barrow to user {}".format(userid,title))

def showAllUsers() :
    filepath = path + "users.dat"
    if os.path.exists(filepath) :          #validation of existed file
        file = open(filepath,"rb")
        users = pickle.load(file)
        print("ID__Name_____LastName___Father___NationalityCode__Birthday\n")
        for i in users :                   #seprated user to show better
            print(i,users[i],"\n")
    else :
        print("no user has been founded")
def showAllBooks() :
    filepath = path + "books.dat"
    if os.path.exists(filepath) :          #validation of existed file
        file = open(filepath,"rb")
        books = pickle.load(file)
        print(" Books Name__Author___Subject___PublishDate\n")
        for i in books :                   #seprated user to show better
            print(i,books[i],"\n")
    else :
        print("no books has been founded")    
def showAllBarrow () :
    filepath = path + "barrow.dat"
    if os.path.exists(filepath) :          #validation of existed file
        file = open(filepath,"rb")
        barrowlist = pickle.load(file)
        print("ID__Name_____LastName___Father___NationalityCode__Birthday\n")
        for i in barrowlist :                   #seprated user to show better
            print("user ID =",i,">>>>>> Book =",barrowlist[i],"\n")
    else :
        print("Barrow list is empty")
# validation of existing dat file
def checkFile(file) :
    filepath= path + file
    if not os.path.exists(filepath) :
        f = open(filepath, "wb+")
        userDict = {}                #intialize a empty dictionary
        pickle.dump(userDict,f)      #write dictionary to bianary file
        f.close()
# body of 
choose = "1"
while choose != 0 :

    os.system("cls")
    print ("1-Add user\n2-Add new book\n3-Search\n4-Barrow\n5-Show all users\n6-Show all books\n7-Show barrow list\n0-Exit\n")
    choose=int(input("Enter your choice : "))
    os.system("cls")

    if choose == 1 :

        #initialize file white filename
        checkFile("users.dat")            

        #get information 
        name=input("Please enter these information\nfirst Name : ")
        fname   =  input("\nLast Name : ")
        birthday = input("\nBirthday : ")
        fathername=input("\nFather Name : ")
        Ncode   =  input("\nNationality Code : ")
        

        #call function
        addUser(name,fname,fathername,Ncode,birthday)

        #Print results 
        print("\n\nthe user sucessfully added !!! ")
        time.sleep(1.5)

    elif choose == 2 :
        # validation of existing file 
        checkFile("books.dat")

        #get information 
        title = input("to add a book you must enter these informations 👇\n Title :")
        author = input("\nautor : ")
        subject = input("\nsubject :")
        year = input("\npublish year :")

        #call function 
        addBook(title, author, subject, year)
        print("\n\nthe Book sucessfully added !!!")
        time.sleep(1.5)

    elif choose == 3 :
        title = input("please enter the tilte : ")
        search(title)
        input("\n\n>>> Press Enter to go main menu <<<")
        os.system("cls")
    
    elif choose == 4 :
        #vatlidation of existing barrow.dat
        checkFile("barrow.dat")

        #get information
        userId = input("Please enter you ID :")
        title = input("Please enter title of chosen book : ")

        #call function 
        barrowBook(userId,title)

        #print result
        print("\n\nthe Book sucessfully barrow to the  !!!")
        time.sleep(1.5)

    elif choose == 5 :
        showAllUsers()
        input("\n\n>>> Press Enter to go main menu <<<")
        os.system("cls")
    elif choose == 6 :
        showAllBooks()
        input("\n\n>>> Press Enter to go main menu <<<")
        os.system("cls")
    elif choose == 7 :
        showAllBarrow()
        input("\n\n>>> Press Enter to go main menu <<<")
        os.system("cls")
