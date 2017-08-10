#!/usr/bin/env python

def hashmap(input_string):
   count = {}
   for s in input_string:
      if count.has_key(s):
         count[s] += 1
      else:
         count[s] = 1
   print count
   for key in count:
      if(count[key] > 1):
           print key, "is repeated", count[key], "times" 
input_string ="Now print the dupe key n times its duped"
hashmap(input_string)
