#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 01:17:17 2017

@author: saurabhmehra
"""

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.Lk = []
        self.Lv = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k not in self.Lk:
            self.Lk.append(k)
            self.Lv.append(v)
        else:
            ind = self.Lk.index(k)
            self.Lk.pop(ind)
            self.Lv.pop(ind)
            self.Lk.append(k)
            self.Lv.append(v)
        
    def getval(self, k):
        """ k, immutable object  """
        try:
            ind = self.Lk.index(k)
            return self.Lv[ind]
        except:
            raise KeyError
        
    def delete(self, k):
        """ k, immutable object """   
        try:
            ind = self.Lk.index(k)
            self.Lk.pop(ind)
            self.Lv.pop(ind)
        except:
            raise KeyError    
        