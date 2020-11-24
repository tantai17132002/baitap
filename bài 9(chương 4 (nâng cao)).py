# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:17:39 2020

@author: tanta
"""

import os
import time
n = "no"
while n == "no":
    n = input("Do you want to Shutdown? (nhập yes hoặc no)")
    if n =="no" :
         time.sleep(30)
    else:
        os.system('shutdown -s')
