#!/usr/bin/env python
import random,string
minimum = input("Please enter the minimum length of any give word to be generated: ")
maximum = input("Please enter the maximum length of any give word to be generated: ")
wmaximum = input("Please enter the max number of words to be generate in the dictionary: ")

alphabet = string.letters[0:52] + string.digits 
string=''
a= []
for count in xrange(0,wmaximum):
   for x in random.sample(alphabet,random.randint(minimum,maximum)):
      string+=x
   print string
   a.append(string)
   string=''
print "array of random words", a
#return a
reverse=""
a1=[]
length=len(a)
for x in range(0,len(a)):
   for y in xrange(len(a[x])):
      reverse = a[x]
      word=reverse[::-1]
   a1.append(word)
print "array of reverse words", a1
#sorted(a1,key=str.upper)
#print a1
for num in range(len(a1)-1,0,-1):
   for i in range(num):
      if a1[i].lower()>a1[i+1].lower():
         temp = a1[i]
         a1[i] = a1[i+1]
         a1[i+1] = temp
print a1
 

