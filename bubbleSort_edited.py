### this is my best
def buble_sort(list):   # bubble sort function
    end = len(list)     # end of array that must to compare
    while end != 0 :    # conter to reach end of array
        for i in range(0,end-1):  # index array picker
            if list[i]>list[i+1] :  # condition
                list[i] , list[i+1] = list[i+1] , list[i] # substitution
        end -= 1        # every time , index of end must be decrease
list = [121,24654,6566,786,47,369,48,647]  # list example to test or function
buble_sort(list) # call function
print(list)  # print our output to see resultssss