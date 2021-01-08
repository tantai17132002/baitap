# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 07:50:23 2021

@author: DELL
"""
    
import numpy as np
from sympy import *

def matran(m,n):
    a = np.random.randint(4,10,(m,n))
    return a

def rank_matran(a):
    b = np.linalg.matrix_rank(a)
    return b

def bac_thang(a):
    b = Matrix(a)
    b_rref = b.rref()
    return np.array(b_rref[0]) 

a = matran(3,4)
r = rank_matran(a)
b = bac_thang(a)
print(a)
print(r)
print(b)