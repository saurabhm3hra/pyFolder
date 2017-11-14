#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 00:07:04 2017

@author: saurabhmehra
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False
    elif len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    
    d1 = {}
    for el in L1:
        if el not in d1:
            if el not in L2:
                return False
            d1[el] = 1
        else:
            d1[el] = d1[el] + 1
    
    d2 = {}
    for el in L2:
        if el not in d2:
            if el not in L1:
                return False
            d2[el] = 1
        else:
            d2[el] = d2[el] + 1
    
    v = 0

    for key in d1.keys():
        if d1[key] != d2[key]:
            return False
        elif d1[key] > v:
            v = d1[key]
            mkey = key
    
    return (mkey, v, type(mkey))