#!/usr/bin/env python

def reverese_word(input_string):
   word = input_string.split(" ")
   print word
   for x in word:
      print x
      x.reversed()
      print ' '.join(word)

input_string="we want to kill you"
reverese_word(input_string)
    
