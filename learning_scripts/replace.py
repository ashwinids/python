#!/usr/bin/env python

def replace_string(input_string):
   str = "x8" 
   for x in input_string:
      if x == " ":
         str += "%20"
      else:
         str += x
   return str
input_string = "we will go to movie today"
replace_string(input_string)
print replace_string(input_string)

