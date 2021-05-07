import hashlib

# functions 
def hash256(password) :                      #hash the generated password
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed

# open file 


# main 
for num in range(0,10000) :   
    file = open ("E:/Python code/github/golden/hashLib/pass.csv")               # gereneting password
    for line in file :                       # read line form file
        tempPass = str.format("%04d"%num)    # 4 digit form generated password
        userDate = line.split(",")           # name and hashed password from file

        if(hash256(tempPass) == userDate[1].rstrip()) :
            print("pass of {} is {}".format(userDate[0],tempPass))