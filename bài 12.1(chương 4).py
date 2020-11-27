# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:21:20 2020

@author: tanta
"""

#1.tạo 1 số nguyên ngẫu nhiên n trong khoảng [50,1000] đóng vai trò là số phần tử của list
import random
n=random.randint(50, 1000)
print([n])

#2.Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]
import random
randomlist = []
n=int(input(" nhập vào số phần tử của list: "))
for a in range (n):
    b = random.randint(-1000,1000)
    randomlist.append(b)
print(randomlist)

#3.Sinh ngẫu nhiên 1 List các số thực tỏng khoảng [-1000.0, 1000.0]
import numpy as np
n = int(input("nhap vao so phan tu cua list= "))
rd = np.random.random_sample(size=n)*-1000.0+1000.0
print("list= ",rd)