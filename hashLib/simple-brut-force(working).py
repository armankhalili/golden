import hashlib

# function
def hash256(password) :
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed

#read file
file = open("E:/Python code/github/golden/hashLib/pass.csv")

# main 
for line in file :
    for num in range (0,10000) :
        tempPass = str.format("%04d"%num)
        userDate = line.split(",")

        if(hash256(tempPass) == userDate[1].rstrip()) :
            print("pass of {} is {}".format(userDate[0],tempPass))