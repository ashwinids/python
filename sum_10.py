#!/usr/bin/env python

def sum():
   print string
   length=len(string)
   for i in range(length):
      for j in range(length):
         if(i != j):
            sum = string[i] + string [j]
            if( sum == 10):
               print string[i], string[j]
n = int(raw_input("enter an array:"))
string = map(int,raw_input().split())
sum()
              
