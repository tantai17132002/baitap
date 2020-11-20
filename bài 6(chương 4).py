# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:38:14 2020

@author: ADMIN
"""

import numpy as np
n = int(input("nhập vào số phần tử của list= "))
rd = np.random.random_sample(size=n)*100
print("list= ", rd)
max = rd[1]
for a in rd:
    if a > max:
        max=a
        print("gia tri lon nhat cua list= ",max)
        
