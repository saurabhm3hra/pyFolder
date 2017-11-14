#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:44:47 2017

@author: saurabhmehra
"""

def genPrimes():
    primes = []
    n = 2
    primes.append(n)
    yield n
    while True:
        n+=1
        for num in primes:
            if n % num == 0:
                break
        else:
            primes.append(n)
            yield n