# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:01:51 2020

@author: tanta
"""

list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for a in list2:
    for b in a:
     print(b)
     for c,d in enumerate(b,2):
         print(c,d,":",b[d])
         
         
         
         