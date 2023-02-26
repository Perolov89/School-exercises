#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# functions handling the users input

def user_input_gender():
    
    while True:

        try:
            gender = int(input('\n\nPress [1] for male or [2] for female: '))
            if gender < 0 or gender > 2:
                raise ValueError
            break
        except ValueError:
            print("\nPlease, input [1] or [2]...")
        
    return gender
            
    
         
def user_input_age():
    
    while True:
        
        try:
            age = int(input('\nHow old is the person? : '))
            if age < 16 :
                raise ValueError
            elif age > 67:
                raise ValueError
            break
        except ValueError:
            print('\nPlease input a valid working age between 16-67. ')
                
    return age
