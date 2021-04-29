def fibo (number):
    if number == 0 or number == 1 :
        return number
    else :
        return fibo(number-1) + fibo(number-2)

variable =int(input("please Enter your number : ")) 
for i in range(0,variable) :
    print(fibo(i)) 