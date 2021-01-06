# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:03:53 2021

@author: DELL
"""

import numpy as np


def ma(n):
    q = np.random.randint(5, 7, (n,n))
    w = np.linalg.det(q)
    e = np.linalg.matrix_rank(q)
    r = q**2
    t = q**3
    return w, e, r, t


m = int(input("nhap m ="))
print(ma(m))

