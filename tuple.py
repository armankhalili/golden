my_tuple = ("apple","orange","lime","lemone")


#### lengh
print(len(my_tuple))
x = list(my_tuple)
x.insert(1,"cucamber")
my_tuple = tuple(x)
print(my_tuple,type(my_tuple))