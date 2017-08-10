#!/usr/bin/env python

class Ashwini:
   def __init__(self):
      self.health = 100
   def eat(self,food):
      if(food == "choclate"):
         self.health -= 50
      elif ( food == "fries"):
         self.health -= 100
      #else:
         #return self.health
food = raw_input("enter food:")
ash = Ashwini()
sri = Ashwini()
print ash.health
print sri.health
ash.eat(food)
print ash.health 
sri.eat("choclate")
print sri.health
        
