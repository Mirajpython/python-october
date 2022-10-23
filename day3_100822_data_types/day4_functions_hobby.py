# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:36:46 2022

@author: meiraj shaik
"""

''' Write a function about your hobby '''
 
   
def guess_hobby(input_var):
    
       
    if input_var.lower() == 'hiking':
        print('You guessed correctly. ')
        print('my hobby is :', input_var)
        guess_result = 'yes'
        
        
    elif input_var.lower() == 'batting':
        print('I am really good at ', input_var)
        print('Yeah U r correct.\n')
        guess_result = 'yes'
        
    
    elif input_var.lower() == 'knittig':
        print('Yes, I love: ', input_var)
        guess_result = 'yes'
        
    elif input_var.lower() == 'swimming':
        print('{0} keeps me fit.'.format(input_var))
        guess_result = 'yes'
        
    else:
        
        guess_result = 'failed'
        
    return guess_result

try_count = 0
while True:
  
  guess_input = input('guess my hobby: ')
  guess_out = guess_hobby(guess_input)
  
  if try_count == 3:
     print("U reached max turns {0}".format(try_count))
     print('Thank u for playing.')
     break
    
  if guess_out == 'yes':
        try_count+=1
        print("Yeah \u2665 We have a winner...\n")
        print("U guessed my hobby {0} in {1} turn(s).".format(guess_input, try_count))
        break
  elif guess_input == 'exit':
     print('Quitting already...')
     break
		
  elif guess_out == 'failed':
        try_count+=1
        print("You failed to guess hobby in {0} turn(s).".format(try_count))
        print("Good Luck next time \n")
        continue
    

    
    
    