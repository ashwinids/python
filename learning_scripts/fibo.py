#!/usr/bin/env python

def fibonacci():
   n = 1
   a = 0
   print n,":",a
   n += 1
   b = 1
   print n,":",b
   n += 1
   while n <= 100:
      fib = a + b
      a,b = b,fib
      print n,":",fib
      n = n + 1
fibonacci()
