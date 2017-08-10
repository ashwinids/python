#!/usr/bin/env python

def merge(A):
   n = len(A)
   if(n<2):
      return
   mid = n/2
   left = A[0:mid]
   right = A[mid:]
   merge(left)
   print(left)	
   merge(right)
   print(right)	
   #length=len(A)
   i=0
   j=0
   k=0
   NL = len(left)
   NR = len(right)
   while(i <= NL and j <= NR):
      if(left[i] < right[j]):
         A[k] = left[i]
         i = i + 1
      else:
         A[k] = right[j]
         j = j + 1
      k = k + 1

   while(i < NL):
      A[k] = left[i]
      i = i + 1
      k = k + 1
   while(j < NR):
      A[k] = right[j]
      j = j + 1
      k = k + 1
   #print("sorted list:", A)
A = [2,3,1,6,8,5,3,7]
merge(A)
print(A)   
   
