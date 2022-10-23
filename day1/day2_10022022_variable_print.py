# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 07:25:02 2022

@author: Miraj Shaik
"""

#hobby = input("enter your hobby:  ")

#print(" highest mountains: "  (hobby = input("what is highest mountain:" )))

def my_hobby1():
    
    print ('I like batmenton')    
    print ('place has to be indoor')
    print ('the site should be hilly')  
    print('The trail should be easy')
    
guess_hobby = input('guess my hobby: ')

def my_hobby2():
    
    hobby_name = input (' what is your hobby: ')
    repeat_times = input(' how many times do you repeat in a month: ')
    place = input('where do you spend it: ')
        
    print (' your hobby is ', hobby_name, 'you are repeating  ', repeat_times, ' times ', 'in the location ', place)    

    
if guess_hobby == 'hiking':
    my_hobby1()
else:
    my_hobby2()
    