#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:58:36 2017

@author: saurabhmehra
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    n = 1
    o = 0
    while True:
        o = o + n
        if o == k:
            return True
        elif o > k:
            return False
        n = n + 1        