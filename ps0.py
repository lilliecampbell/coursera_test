# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:37:36 2020

@author: Lillie Campbell
"""

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
first = x**y
print("x**y = ", first)
import numpy
second = int(numpy.log2(x))
print("log(x) = ", second)