#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 00:32:25 2017

@author: saurabhmehra
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    uL = []
    rL = []
    for key in aDict.keys():
        if (aDict[key] not in uL):
            if(aDict[key] not in rL):
                uL.append(aDict[key])
        else:
            uL.remove(aDict[key])
            rL.append(aDict[key])
    
    uK = []
    for key in aDict.keys():
        if aDict[key] in uL:
            uK.append(key)
    
    uK.sort()
    return uK