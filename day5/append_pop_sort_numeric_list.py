# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 08:01:57 2022

@author: Miraj Shaik
"""

import sys

my_list = []

def list_ops():
    
    menu = '\n\n'
    menu += 'append: Append to a list \n'
    menu += 'pop: pop an item from Top of the list \n'
    menu += 'select: pop an item at index  \n'
    menu += 'insert: Insert at Index value \n'
    menu += 'exit: Quit from the program \n'
    menu += 'sort: Sort the list \n'
    menu += 'print: Print the list \n'
    
    print(menu, end='\n')

def append_list():
    print ('enter "done" to quit fromt the list: \n\n' )
    while True:
         get_item = input('Enter anything : ')
         
         if get_item == 'done':
            print('list completed: \n')
            print( 'Number of items in a list is:', len(my_list), end='\n\n')
            print('list is :', my_list, end='\n\n')
            break
         else:
            try:
             # Convert it into integer    
             my_list.append(int(get_item))
             continue
            #this is exception handling when entered non-numeric value
            except ValueError:
               try:
                   #num_item = float(get_item)
                   my_list.append(float(get_item))
                   continue
                  #this is exception handling when entered value is string
               except ValueError:
                  print('You entered a string item to the list: ')
                  print('please enter a numeric item to the list: ')
                  continue
    
def pop_list():    
      if len(my_list) == 0:
          print('the list is empty, please select "append" to add something to the list')
          
      while len(my_list) > 0:
        print('startig poping items from the list')
        print('Popping ', my_list.pop())
        print('my list is:', my_list)
                
def pop_select():
      if len(my_list) == 0:
          print('the list is empty, please select append to add something to the list')
 
      while len(my_list) > 0:
        print('the current list is: ', my_list)
        print('Enter 200 to go out of the loop')
        pop_item = int(input('what index to remove item from: '))
        if pop_item.__eq__(200):
           break
        print('Removing: {0} '.format(my_list.pop(pop_item)))
        print('Remaining List: {0}'.format(my_list), end='\n\n')
        

        
def insert_list():
    while True:
        print('the current list is: ', my_list)
        ask_index = input('Index please: ')
        ask_item = input('Insert Item please: ')
        
        try:
             my_list.insert(int(ask_index), int(ask_item))
             print('the updated list is: ', my_list)
             break
        
        except IndexError as err:
            print('Index error: {0}'.format(err))
            
        except ValueError:
            try:
                my_list.insert(int(ask_index), float(ask_item))
                print('the updated list is: ', my_list)
                break
            
            except ValueError:
                  print('You entered a string item to the list: ')
                  print('please enter a numeric item to the list: ')
                  continue
              
def sort_list():
     if len(my_list) == 0:
         print('the list is empty, please select append or insert to add something')
     else:   
         print('the current list is : ', my_list)
         my_list.sort()
         print('the sorted list default order is : ', my_list)
         my_list.sort(reverse=True)
         print('the sorted list in descending order is : ', my_list)

def print_list():
     if len(my_list) == 0:
         print('the list is empty, please select append or insert to add something')
     else:   
         print('the current list is : ', my_list)
                        

''' start calling my functions '''

''' start of Main program '''

def main():
  while True:
    
    
    try:
        
        list_ops()
        oper = input('Enter Operation: ')
        
        if oper.__eq__('exit'):
            sys.exit(0)
            
        if oper.__eq__('append'):
           append_list()
                   
        elif oper.__eq__('pop'):
             pop_list()
            
        elif oper.__eq__('select'):
            pop_select()
            
        elif oper == 'insert':
            insert_list()
            
        elif oper.__eq__('sort'):
            sort_list()
            
        elif oper.__eq__('print'):
            print_list()
            
    except (IOError, InterruptedError, TypeError ):
        sys.exit('Encountered an Error, Exiting.')
    
if __name__ == "__main__":
    
    main()

