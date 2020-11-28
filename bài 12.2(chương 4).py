# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:50:09 2020

@author: tanta
"""

import random,string
x=random.randint(2, 10)
letters = string.ascii_lowercase 
n = ''.join(random.choice(letters) for i in range(x))
m=random.randint(0, 100)
proboy={'name': n,'age': m }
print("dictionary= ",proboy)
