"""
Created on Wed Jul 5 23:56:23 2023

@author: LameUser
"""

import os


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        

def write_file(path, data):
    f = open(path,'w')
    f.write(data)
    f.close()
    
