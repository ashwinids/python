#!/usr/bin/env python

def hashmap(input_string):
   count = {}
   A = True
   for s in input_string:
      if count.has_key(s):
         A = False
      else:
         count[s] = 1
   if(A == True):
       print" string is unique"
   else:
      print " string is not unique"
input_string = "Ashwin45555555ash"
hashmap(input_string)     
