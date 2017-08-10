#!/usr/bin/env python

import sys
import os
import random

grocery_list=['fruits', 'juices', 'veggies']
print(grocery_list[0])
print(grocery_list[0:2])

other_events=[ 'car', 'wash', 'sweets']
print(grocery_list+other_events)
todo_list = [grocery_list, other_events]
print(todo_list)
grocery_list.append('onions')
grocery_list.insert(1, 'orange')
grocery_list.reverse()
print(todo_list)
print(len(todo_list))
family_dic = { 'brothers' : '3', 
		'sisters' : '4',
		 'uncles' : '5'}
print(family_dic.get('brothers'))
