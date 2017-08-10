#!/usr/bin/env python

def fib():
   i = 0
   j = 1
   n = 1
   print n," :", i
   n += 1
   print n," :", j
   n += 1
   while (n <= 10):
      sum = i + j
      i = j
      j = sum
      print n," :", sum
      n = n + 1
fib()
