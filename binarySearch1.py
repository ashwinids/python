#!/usr/bin/env python

def binary():
   length = len(string)
   found = 0
   start = 0
   end = length - 1
   while (start <= end ):
      print start
      print end
      mid = (start+end)/2
      print mid
      print string[mid]
      print var
      if(var == string[mid]):
         found = 1
         break
      elif (var > string[mid]):
          start = mid + 1
      elif (var < string[mid]):
          end = mid - 1
   if (found==0):
      print " not present"
   else:
      print " present "
   
string = [ 1, 2, 3, 4, 5, 7, 8, 9]
var=int(raw_input("enter a number:"))
binary()  
         
         

