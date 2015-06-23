#! /usr/bin/env python

"""
This is a python module that converts temperature
"""

def f_to_k(temp):
   converted = ((temp-32.0)*(5.0/9))+273.15
   return converted

print f_to_k(32)
print f_to_k(212)
