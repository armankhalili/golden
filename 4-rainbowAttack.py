import hashlib,random

randomHashedPassword = hashlib.sha256(chr(random.randrange(0000,9999)).encode("utf-8")).hexdigest()   #  hashed a random number in range 0000 to 9999 by encode utf-8 and hexdigest

for i in range(0000,9999) :
    guess = hashlib.sha256(chr(i).encode("utf-8")).hexdigest()
    if guess == randomHashedPassword :
        print( " the password is : ",i)
    else :
        pass
