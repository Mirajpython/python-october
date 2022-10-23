## Function to tell a message as per age
def age_group(your_age):
    
    if your_age > 60:
        message = 'too_old'
    elif your_age > 30 and your_age <= 60:
        message = 'U must be stable. Starting looking at your 401k'  
    elif your_age == 30:
        message = 'Get a degree - go biking'        
    elif your_age > 25 and your_age < 30:
        message = 'enjoy_life. don\'t worry'
    elif your_age > 20 and your_age <= 25:
       message = 'U played enough. get it together'    
    else:
        message = 'you have engough time to play'
# this return passing out put to main program       
    return message   
 
while True:
#input statement to ask your age  
   get_age = input('Please Enter your age: ')
      
   try:
     # Convert it into integer    
       valid_age = int(get_age)
       print('you Entered a numeric value to age: ', valid_age)
     # calling age_group function based on input value to age
       valid_age1 = age_group(valid_age) 
    # printing message got from function
       print(valid_age1)
       break
    #this is exception handling when entered non-numeric value
   except ValueError:
         try:
           # Convert it into float
             valid_age = float(get_age)
             print('You entered a floting number to age: ', valid_age)
             print('please enter a numeric value: ')
             continue
            #this is exception handling when entered value is string
         except ValueError:
            print('You entered a string  to age: ')
            print('please enter a numeric value to age: ')
            continue
