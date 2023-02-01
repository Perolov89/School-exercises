#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

while True:
    user_choice = input("Välj mellan sten,sax, påse:")
    possiable_input = ('sten', 'sax', 'påse')
    computer_choice = random.choice(possiable_input)
    print(f"\nDu valde {user_choice}, datorn valde {computer_choice}.\n")


    if user_choice == computer_choice:
        print(f"Båda valde {user_choice}. Det är lika!!")
    elif user_choice == "sten":
        if computer_choice == "sax":
            print("Sten krossar sax! Du vann!")
        else:
            print("Stenen läggs i påsen! Du förlorade.")
    elif user_choice == "påse":
        if computer_choice == "sten":
            print("Stenen läggs i påsen! Du vann!")
        else:
            print("Sax klipper paper! Du förlorade.")
    elif user_choice == "sax":
        if computer_choice == "papper":
            print("Sax klipper papper! Du vann!")
        else:
            print("Sten krossar sax! Du förlorade.") 
            
    play_again = input("Spela igen? (j/n): ")
    if play_again.lower() != "j":
     break