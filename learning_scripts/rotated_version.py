#!/usr/bin/env python

def rotate():
   if len(array1) != len(array2):
      return False
   for i in range(len(array1)):
      c= array1[-i:] + array1[:-i]
      print c
      if array2 == c:
         return True
   return False 
array1=[1,2,3,5,6,7,8]
array2=[5,6,7,8,1,2,3]
rotate()   
print rotate()
