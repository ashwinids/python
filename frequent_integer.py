#!/usr/bin/env python

def frequent():
   count = {}
   for i in array:
      if count.has_key(i):
         count[i] += 1
      else:
         count[i] = 1
   print count
   print max(count, key=count.get)
   #length=len(count)-1
   #print length
   #for i in range(len(count)):
    #  print count[i]
    #  if count[i] > count[i+1]:
     #    count[i],count[i+1] = count[i+1],count[i]
   #print count
    
array = [ 1, 4, 4, 5, 5, 5, 6]
frequent()
#print frequent()       
