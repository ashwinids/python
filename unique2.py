#!/usr/bin/env python

def unique(input_string):
   length = len(input_string)
   print(length)
   if length > 36:
      print("not unique")
   A = True
   for i in range(0,length):
      #print(input_string[i])
      for j in range(i+1,length):
         #print(input_string[j])
         if(input_string[i] == input_string[j]):
            A =  False
   if(A == False):
      print " not unique"
   else:
      print"unique"  

input_string = "Ashwini45"
unique(input_string)
