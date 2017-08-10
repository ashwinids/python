#!/usr/bin/env python

class Employee:
   def __init__(self, Name, Salary):
      self.name = Name
      self.salary = Salary 
   def departmentA(self):
      self.name[0] = self.salary[0]
      self.name[3] = self.salary[3]
   def departmentB(self):
      self.name[2] = self.salary[2]
name = [ tm, sam, kevin, harry, tim ]
salary = [ 100, 200, 300, 400, 500 ] 
A = Employee(name,salary)
B = Employee()
print A.departmentA()
print B.departmentB()

