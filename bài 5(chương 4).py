# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:48:15 2020

@author: ADMIN
"""

a=[0, 1, 2, 3.5, 4, 5, 6]
n=1
import math
for b in a:
    print(" giá trị phần tử thứ ",n, "=", b)
    n+=1
    if b>0:
        print("logarit tự nhiên phần tử thứ ",n, "=", math.log(b))
    else:
        print("Không có logarit phần thử thứ n")
    



