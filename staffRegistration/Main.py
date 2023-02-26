#!/usr/bin/env python3
# -*- coding: utf-8 -*-

males = 0
females = 0
maleAge = 0
femaleAge = 0
averageFemaleAge = 0
averageMaleAge = 0
answer = 'y'

from check_user_input import user_input_gender, user_input_age

print('\nWelcome to staff registration!\nPlease follow the steps to add a new staff member...')
           
while answer == 'y':
        gender = user_input_gender()
         
        if gender == 1:
            males += 1
        elif gender == 2:
            females += 1


        age = user_input_age()
             
        if gender == 1:
            maleAge += age
            averageMaleAge = maleAge // males   
        elif gender == 2:
            femaleAge += age
            averageFemaleAge = femaleAge // females
        
            
        print(f"\nCurrent staff: {males} males and {females} females")
        print(f'\nThe average age of males are: {averageMaleAge}\nThe average age of females are: {averageFemaleAge}')
        answer = input('\nPress [y] if you want to add another person\nPress [n] if you want to quit:')
print('\nThank you for using the staff registration program.')
            
            