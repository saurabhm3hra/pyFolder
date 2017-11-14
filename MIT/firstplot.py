# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pylab as plt

samples = [1,2,3,4,5,6,7]
lin = [1,2,3,4,5,6,7]
quad = [1,4,9,16,25,36,49]

plt.figure('lin1')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(samples, lin)

plt.figure('quad')
plt.plot(samples, quad)
