# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:50:13 2020

@author: tanta
"""

#1.Tạo ngẫu nhiên số  phần tử của List  50 <= n <= 100
import numpy as np
import random
n = random.randint(50,100)
rd = np.random.random_sample(size=n)*10000-10000
print("list1 = ",rd)


#2. Tạo ngẫu nhiên List gồm n phần tử với cấu trúc sau: [{'name': ' sinh ngẫu nhiên', 'age': 'sinh ngẫu nhiên'}] có tất cả n dictionary như trên trong List.
import random,string
x = random.randint(2,50)
z= list()
for i in range (x):
    y = random.randint(2,10)
    t = random.choice(string.ascii_uppercase)
    h = t+ ''.join(random.choice(string.ascii_lowercase) for i in range (y))
    m = random.randint(0, 100)
    k = [{'name':h, 'age':m}] 
    z.extend(k) 
print("list 2= ",z)

