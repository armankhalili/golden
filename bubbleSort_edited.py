### this is my best
def buble_sort(list):
    end = len(list)
    while end != 0 :
        for i in range(0,end-1):
            if list[i]>list[i+1] :
                list[i] , list[i+1] = list[i+1] , list[i]
        end -= 1        
list = [121,24654,6566,786,47,369,48,647]
buble_sort(list)
print(list)