#!/usr/bin/env python

def anagram(s):
   count = {}
   for x in s:
      if count.has_key(x):
         count[x] =+ 1
      else:
         count[x] = 1
   return count
st1 = "silent"
st2 = "listen"
a = anagram(st1)
b = anagram(st2)
if (a == b):
   print "strings are anagram"
else:
   print " strings are not anagram"


   
