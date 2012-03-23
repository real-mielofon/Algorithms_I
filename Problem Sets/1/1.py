'''
Created on 23.03.2012

@author: Alexey
'''

import math
def fa(n):
    return math.sqrt(n)

def fb(n):
    return 10**n

def fc(n):
    return n**1.5

def fd(n):
    return 2**math.sqrt(math.log(n))

def fe(n):
    return n**(5/3)

n = 200000
print 'a=',fa(n)
#print 'b=',fb(n)
print 'c=',fc(n)
print 'd=',fd(n)
print 'e=',fe(n)

#print fb(n) > 
print fc(n) > fe(n) > fa(n) > fd(n)