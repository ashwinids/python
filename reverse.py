#!/usr/bin/env python


def reverse(input_string):
   reverse_string = [ ]
   length = len(input_string)
   count = 0
   for i in range(0, length):
      reverse_string.append(input_string[length-1 - count])
      count += 1
   reverse_string = "".join(reverse_string)
   print reverse_string
input_string = "I want to kill you"
reverse(input_string) 
  
