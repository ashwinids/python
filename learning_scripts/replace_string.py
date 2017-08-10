#!/usr/bin/env python

def replace():
   words = string.split()
   #print words
   str = ""
   length = len(words)
   #print "length", length
   for i in range(0,length):
      if(words[i] == input):
         #print words[i]
         #print input
         str += ""
      else:
         #print words[i]
         str += words[i]
         str += " "
   return str

string=raw_input("enter string:")
input=raw_input("enter word: ")
replace() 
print replace()
