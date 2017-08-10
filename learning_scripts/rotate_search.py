#!/usr/bin/env python

def search():
   start = 0
   end = len(array)-1
   for i in range(len(array)):
      array1 = array[-i:] + array[:-i]
      mid = (start + end)/2
      if (array1[mid] < array1[end]):
         break
   print array1
   present = 0
   while(start <= end):
      mid = (start+end)/2
      if (var == array1[mid]):
         present = 1
         break
      if (var > array1[mid] ):
         start = mid + 1
      elif (var < array1[mid]):
         end = mid - 1
   if (present == 0):
      print "not present"
   else:
      print "present"
array=[5,6,7,8,1,2,3]
var = int(raw_input("enter a num:"))
search()     
