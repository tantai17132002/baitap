# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:32:34 2020

@author: tanta
"""

import os
import time
shutdown = True
while shutdown:
    shutdown = input("Do you want to Shutdown? (nhập yes hoặc no) ")
    if shutdown =="yes" :
        os.system('shutdown -s')
        shutdow = False                 
    else:
        print("chờ 1 lát rồi được hỏi lại")
        time.sleep(30)
        shutdown = True