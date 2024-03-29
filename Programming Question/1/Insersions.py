'''
Created on 18.03.2012

@author: Alexey

Question 1
Download the text file here. (Right click and save link as)
The file contains all the 100,000 integers between 1 and 100,000 (including both) in some random order( no integer is repeated).

Your task is to find the number of inversions in the file given (every row has a single integer between 1 and 100,000). Assume your array is from 1 to 100,000 and ith row of the file gives you the ith entry of the array.
Write a program and run over the file given. The numeric answer should be written in the space.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make upto 5 attempts, and we'll count the best one for grading.
(We do not require you to submit your code, so feel free to choose the programming language of your choice, just type the numeric answer in the following space)

'''
def brut_fopce(lines):
    c = 0
    pairs = []
    for i in range(0,len(lines)):
      for j in range(i+1,len(lines)):
        if lines[i] > lines[j]:
            c = c + 1
    return c

def merge_sort_split(list1, list2):
    result = []
    i, j = 0, 0
    c = 0
    for k in range(0, len(list1) + len(list2)):
        if (j >= len(list2)) or ((i < len(list1)) and (list1[i] <= list2[j])):
            result.append(list1[i])
            i = i + 1
        else: 
            result.append(list2[j])
            for u in range(i, len(list1)):
                if list1[u] <= list2[j]:
                    break
                c = c + 1
            j = j + 1
    return result, c 
    
def merge_sort_count(list):
    if len(list) <= 1:
        return list, 0
    else:
        n = len(list) // 2
        
        sort1, x = merge_sort_count(list[:n])
        sort2, y = merge_sort_count(list[n:])

        sort, z = merge_sort_split(sort1, sort2)
        
        return sort, x+y+z


def create_lines_from_file():
    f = open('IntegerArray.txt', 'r')
    lines_s = f.readlines()
    lines = []
    for l in lines_s:
        lines.append(int(l))
    
    return lines


def create_lines_down(num):
    lines = []
    for i in range(num, 0, -1):
        lines.append(i)
    
    return lines

def create_lines_up(num):
    lines = []
    for i in range(0, num):
        lines.append(i)
    
    return lines


def create_lines_random_merge(num):
    lines = []
    for i in range(0, num):
        lines.append(i)
    for i in range(0, 2*num):
        k,n = random.randrange(num), random.randrange(num)
        lines[k], lines[n] = lines[n], lines[k]
    
    return lines

import random

def create_lines_random(num):
    lines = []
    for i in range(0, num):
        lines.append(random.randrange(num))
    
    return lines


import winsound
if __name__ == '__main__':
    lines= create_lines_from_file()
#    lines= create_lines_random(60000)
#    lines= create_lines_random_merge(200)
#    lines = [1, 3, 0, 5, 4, 2]
#    lines= create_lines_down(2000)
#    lines = [1,3,5,2,4,6]

    print "(%d, %d)="%(len(lines), len(lines)*(len(lines)-1)/2), lines

    sortlines, c = merge_sort_count(lines)
    print " " #2397810677
    print c #2397810677

    c = brut_fopce(lines)
    print " " #2397810677
    print c #2397810677

    
