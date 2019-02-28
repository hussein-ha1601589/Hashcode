#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:01:53 2019

@author: hamza
"""

import numpy as np
common = lambda x, y : np.prod(np.intersect1d(x, y).shape)

x = np.array(['t1','t2','t3','t4','t5','t6'])
y= np.array(['t3','t4','t5','t6','t7','t8','t9','t10'])


in1 =  lambda x, y : np.prod(np.setdiff1d(x,y).shape)
print(in1(x,y))
print(in1(y,x))

print(common(x,y))

interest = lambda x,y : min(common(x,y),in1(x,y),in1(y,x))


print(interest(x,y))






