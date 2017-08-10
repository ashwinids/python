#!/usr/bin/env python

def alpha():
   count_lower=0
   count_upper=0
   count_numeric=0
   for i in string:
      if(i.islower()):
         count_lower+=1
      elif(i.isupper()):
         count_upper+=1
      elif(i.isdigit()):
         count_numeric+=1
   print "lower case:", count_lower
   print "upper case:", count_upper
   print "number:", count_numeric 
string = raw_input("enter a string:")   
alpha()
