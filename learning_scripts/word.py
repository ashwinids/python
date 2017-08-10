#!/usr/bin/env python
import random,string

from string import ascii_lowercase

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = [ c for c in ascii_lowercase if c not in VOWELS] + ['']*2

def random_word():
   """ Returns a random word composed of consonants and vowels """
   word = ''
   random_range = random.randint(3,4)  
   for i in range(random_range):
      word += random.choice(VOWELS) + random.choice(CONSONANTS)
   print word
random_word()
