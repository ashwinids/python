#!/usr/bin/env python

def unique(input_string):
   length = len(input_string)
   print(length)
   if length > 36:
      print("not unique")
   for i in range(0,length):
      #print(input_string[i])
      for j in range(i+1,length):
         #print(input_string[j]) 
         if(input_string[i] == input_string[j]):
            return False
   return True


input_string = "Ashwin45"
A=unique(input_string)
print(A)
if(A == False):
   print" String is not unique"
else:
   print"string is unique"   
  
   
