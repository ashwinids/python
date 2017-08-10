#!/usr/bin/env python

class Employee:
   def __init__(self, Name, Salary):
      self.name = Name
      self.salary = Salary 
   def displayEmployee(self):
      print "Name :", self.name, ",Salary:", self.salary
emp1 = Employee("Ash", 5000)
emp2 = Employee("Adu", 6000)
emp1.displayEmployee()
emp2.displayEmployee()    
