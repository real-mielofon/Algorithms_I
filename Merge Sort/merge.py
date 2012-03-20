'''
Created on 18.03.2012

@author: Alexey
'''

import random

def merge(list1, list2):
    result = []
    i,j = 0,0
    while ((i < len(list1)) or (j < len(list2))): 
        if (j >= len(list2)) or ( (i < len(list1)) and (list1[i] < list2[j])):
            result.append(list1[i]);
            i = i+1
        else:
            result.append(list2[j]);
            j = j+1
    return result

def sort(list):
    if len(list) <= 1:
        return list
    else:
        n = len(list) // 2
        result = merge(sort(list[0:n]), sort(list[n:]))
        return result 

def main():
    
    list = [51, 70, 72, 67, 57, 59, 52, 0, 83, 77, 32, 90, 54, 64, 35, 92, 46, 99, 42, 27, 55, 80, 42, 80, 3, 44, 33, 91, 78, 19, 73, 7, 18, 36, 8, 23, 1, 67, 34, 93, 87, 45, 75, 83, 84, 5, 38, 20, 71, 4, 16, 52, 14, 83, 25, 45, 93, 75, 31, 11, 45, 92, 51, 7, 86, 11, 11, 52, 65, 12, 47, 0, 18, 67, 89, 25, 29, 72, 70, 50, 48, 40, 89, 2, 75, 41, 79, 5, 20, 30, 33, 92, 36, 48, 51, 56, 33, 66, 15]

#    for i in range(1,100):
#        list.append(random.randint(0,100))
        
    print "sl1(",len(list),")=", list
    print sort(list)
       

if __name__ == '__main__':
    main()