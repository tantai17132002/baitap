# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 23:38:58 2020

@author: tanta
"""

import numpy as np
n = int(input("nhap vao so phan tu cua list= "))
rd = np.random.random_sample(size=n)*10000-10000
print("list= ",rd)
min = rd[1]
for b in rd:
    if b < min:
        min = b
        print("gia tri nho nhat cua list= ",min)
        
        

                 


