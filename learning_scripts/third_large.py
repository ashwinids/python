#!/usr/bin/env python

def largest(A):
   n = len(A)
   first = A[0]
   second = A[1]
   third = A[2]
   for i in range(0,n):
      if(first < A[i]):
         second = first
         third = second
         first = A[i]
      elif(A[i] > second):
         third = second
         second = A[i]
      elif(A[i] > third):
         third = A[i]
   print(third)
A = [ 3, 4, 5, 9, 7, 8]
largest(A)
                
     
   
