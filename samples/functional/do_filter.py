#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


from functools import reduce
def is_palindrome(n):
    L=[]
    N=n
    while True:
        L.append(N%10)
        if N//10==0:
            break
        else:
            N=N//10
    output=reduce(lambda x,y:x*10+y,L)
    return output==n




def is_palindrome(n):
	return str(n)==str(n)[::-1]
 
output = filter(is_palindrome, range(1, 1000))
print(list(output))
