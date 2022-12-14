# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 07:46:35 2022

@author: meera
"""

import datecheck
import shelve
import os
import datetime
import inspect


filename = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
filename = str(filename) + '/birthdaysfile'
def addinlist():
    adddate = shelve.open(filename, writeback=True)
    print("Please enter the name of person: ", end='')
    name = input()
    print("Please give his birthday date (in format dd/mm): ", end='')
    Date = input()
    Date = datecheck.validate(Date)
    if Date != 'FALSE':
        adddate['birthdays'][name.title()] = Date
        print("\n" + name.title() + ": " + adddate['birthdays'][name.title()], end='')
        print(" added\n")
    else:
        print("Error!!! \nInvalid Date")
    adddate.close()


def deleteinlist():
    deldate = shelve.open(filename, writeback=True)
    print("Enter the name of the person you want to delete: ", end='')
    name = input()
    try:
        print( name.title() + ": " + deldate['birthdays'][name.title()] + ' deleted from database\n')
        del(deldate['birthdays'][name.title()])
    except KeyError:
        print("Sorry! The person is not in the list\n")
    deldate.close()


def checkbyname():
    checkbirthday = shelve.open(filename)
    print("Please Enter the Name of the person:", end='')
    name = input()
    if name.title() in checkbirthday['birthdays'].keys():
        print(name.title() + ": " + checkbirthday['birthdays'][name.title()] + "\n")
    else:
        print("Sorry! Person is Not in the list\n")
    checkbirthday.close()


def checkbydate():
    retbydate = shelve.open(filename)
    print("Please enter the birthday date to check (in format dd/mm): ", end='')
    Date = input()
    Date = datecheck.validate(Date)
    flag = 0
    if Date != 'FALSE':
        for name, chkDate in retbydate['birthdays'].items():
            if Date == chkDate:
                print(name.title() + ": " + chkDate)
                flag = 1
        if flag == 0:
            print("Sorry ! No one with given birth date present in the database")
    else:
        print("ERROR!!! Invalid Date")
    retbydate.close()
    print("")

def printlist():
    printdays = shelve.open(filename)
    count = 0
    for name, date in printdays['birthdays'].items():
        print(name.title() + ": " + date)
        count = count + 1
    if count == 0:
        print("No person in the list")
    print("\n")
    printdays.close()

if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')

start = shelve.open(filename)
currDate = str(datetime.date.today())[-2:] + '/' + str(datetime.date.today())[-5:-3]
currDate = datecheck.validate(currDate)
print("Today is : ", end='')
flag = 0
print(currDate)
try:
    for name, date in start['birthdays'].items():
        if start['birthdays'][name] == currDate:
            print("\t" + name)
            flag = 1
except:
    start['birthdays']={}
start.close()
if flag == 0:
    print("No one's", end=' ')
print("Birthday")
print("\nWant to continue ? (Press y for yes): ", end='')
ch = input()

if(ch != 'y'):
    exit(0)
print("\n\nWelcome to Birthday Reminder\n")

choices = 5
cont = 'c'

while cont == 'c':
    choice = 0
    print("\nWhat do you want to do ? (press the corresponding choice no.) \n")
    print("1. Add a new person's birthday in the list.")
    print("2. Delete a person's birthday from your list.")
    print("3. Check a person's birthday from his name.")
    print("4. Check if anyone has birthday on a particular date.")
    print("5. Print the whole list")
    while choice <= 0 or choice > choices:
        print(f"\nPlease enter a valid input of choice between 1 and {choices}")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
    print("OK \n")
    if choice == 1:
        addinlist()
    elif choice == 2:
        deleteinlist()
    elif choice == 3:
        checkbyname()
    elif choice == 4:
        checkbydate()
    else:
        printlist()

    print("Do you want to continue or exit ? (press c to continue)")
    cont = input()