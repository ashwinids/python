#!/usr/bin/env python

def binary(num):
   string=""
   flag = True
   while flag:
      remainder = num % 2
      quotient = num / 2
      if quotient == 0:
         flag = False
      string += str(remainder)
      num = quotient
      
   string = string[::-1]
   return string
num = int(raw_input("enter a num:"))
binary(num)
print binary(num)        

