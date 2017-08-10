#!/usr/bin/env python

def permutation(str):
  l=[]
  for i in range(len(str)):
     m=str[i]
     print m
     remlist= str[:i] + str[i+1:]
     print remlist
     for p in permutation(remlist):
        l.append([m] + p)
  print l

str="ABC"
permutation(str)
print permutation(str)   
