# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 07:21:55 2022

@author: meiraj Shaik
### print the list of item collected from user entered
"""

item_list = []


while True:
    
    ask_user = input('Please enter something: ')
    if str(ask_user) == 'exit':
        print('you have completed the list...')
        print('The list is:\n', item_list)
        break   
    
    else:
        item_list.append(ask_user)
        print('The list is:\n', item_list)
        continue
        
        
        
        