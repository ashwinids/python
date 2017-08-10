#!/usr/bin/env python

def prime():
   c=1
   i = 1
   while (c <= n):
      if (i%2 != 0):
          print c, ":", i
          i = i+1
          c = c + 1
      else:
         i = i + 1
          
n = int(raw_input("enter n:"))
prime()
