#!/usr/bin/env python
import random
import string
def reverse():
   for i in range(0,10):
      random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
      print random
reverse()










