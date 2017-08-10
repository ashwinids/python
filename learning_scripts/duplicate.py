#!/usr/bin/env python

def remove_dups(input_string):
   list = []
   length=len(input_string)
   for i in range(0,length):
      if input_string[i] not in list:
         list.append(input_string[i])
   print list
input_string= "Ashwini"
remove_dups(input_string)
        
