#!/usr/bin/env python

def largest(a,b,c):
   if(a > b and a > c):
      print"the largest num is", a
   elif(b > a and b > c):
      print"the largest num is", b
   else:
      print"the largest num is ", c
a = raw_input("enter a:")
b = raw_input("enter b:")
c = raw_input("enter c:")
largest(a,b,c) 
