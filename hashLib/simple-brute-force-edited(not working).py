import hashlib

# functions 
def hash256(password) :
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed

# open file 
file = open ("E:/Python code/github/golden/hashLib/pass.csv")

# main 
for num in range(0,10000) :
    for line in file :
        tempPass = str.format("%04d"%num)   # 4 digit generated password
        userData = line.split(",")      # name and hashed password from file

        if(hash256(tempPass) == userData[1].rstrip()) :
            print("pass of {} is {}".format(userData[0],tempPass))