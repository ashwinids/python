#!/usr/bin/env python
import random
def main():
   print("guess the number between 1 to 100")
  # randomNumber = 35 this for debugging
   randomNumber = random.randint(1,100)
   found=False
   while not found:  
      userguess = input("your guess: ")
      if userguess == randomNumber:
         print("you got it")
         found=True
      elif userguess > randomNumber:
         print("guess lower!")
      else:
         print("guess higher!")

   print "Thanks for playing our game"
main()

