path = 'E:/Education/CWNA.txt'
myfile = open(path, 'r',encoding='utf-8')


                   ### read line

Lines = myfile.readlines()

print ("\n MY new list line : ", Lines ,"\n number of lines of my file : ", len(Lines) )

                   ## write file 

path2 = 'E:/Education/file.txt'
myfile = open(path2, 'w+',encoding='utf-8')

message = "firt writte python string to a file"

myfile.write(message)

                    ### append string to a file 

path3 = 'E:/Education/file.txt'
myfile = open(path3, 'a',encoding='utf-8')   

for i in range(1,100) :
    string = i
    if i < 10 :
        string = "0{}".format(i)
    text = "\n {} == line of file ".format(string)
    myfile.write(text)

                      ### file exist 
import os 

path3 = 'E:/Education/file3.txt'
filename = path3.split("/")
if os.path.exists(path3) :
    print("\nthe {} is exists ".format(filename[-1]))
else :
    print("\nthe {} is not exists ".format(filename[-1]))