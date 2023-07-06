"""
Created on Wed Jul 5 23:56:23 2023

@author: LameUser
"""

import os
import linecache

def get_ip_address(url):
   command = "nslookup " + url + ' 1.1.1.1'
   process = os.popen(command)
   results = (process.read())
   marker = results.find('Addresses:') 
   return results[marker:].splitlines()[0]
url = input('Enter url: ')
print(get_ip_address(url))

