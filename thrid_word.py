#!/usr/bin/env python
import re
string=raw_input("enter string:")
words=string.split()
b=""
for i in range(1,len(words)+1):
   if(i%3==0):
      b += words[i-1]
      b += " "
print b      
