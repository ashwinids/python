#!/usr/bin/env python

#additin
def add(num1, num2):
   return num1 + num2
#subtraction
def sub(num1, num2):
   return num1 - num2
#multiplication
def multi(num1, num2):
   return num1 * num2
#devision
def divide(num1, num2):
   return num1 / num2

def main():
   operation = raw_input("what u want to do (+,-,*,/):")
   if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
      print("enter the valid operation")
   else: 
      num1 = int(raw_input("enter num1:"))
      num2 = int(raw_input("enter num2:"))
      if(operation == "+"):
         print(add(num1, num2))
      elif(operation == "-"):
         print(sub(num1, num2))
      elif(operation == "*"):
         print(multi(num1, num2))
      else:
         print(divide(num1, num2))  
main()          

