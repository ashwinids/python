#!/usr/bin/env python

def alpha():
   length=len(string)
   b=""
   for i in range(length):
      if(i%3 == 0):
         b+=string[i]
   print b      
string=raw_input("enter the string:")
alpha()

