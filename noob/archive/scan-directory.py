# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:34:36 2018

@author: Vipul
"""

import os
for root, dirs, files in os.walk("./new-folder", topdown = True):
    
    for filename in files:
        # print(os.path.join(root, filename))
        print("FILE: " + filename)
        
    for dirname in dirs:
        print("DIRECTORY: " + dirname)