# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:19:30 2018

@author: Vipul
"""

import os

dirname = "new-folder"

if not os.path.exists(dirname):
    os.mkdir(dirname)
    print("Directory ", dirname, " created!")
else:
    print("Directory ", dirname, " already exists!")

'''
if not os.path.exists(os.getcwd() + "/" + dirname):
    os.mkdir(os.getcwd() + "/" + dirname)
    print("Directory ", dirname, " created!")
else:
    print("Directory ", dirname, " already exists!")
'''
