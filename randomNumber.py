import os
import sys
import random


def get_random_number(): 
    try: 
        in_range = int(input("Enter Number 1: "))
        in_range2 = int(input("Enter Number 2: "))

        if in_range > in_range2:
            print("Number 2 should be higher than number 1, Please try again")
            get_random_number()
        
        randomNumber = random.randint(int(in_range),int(in_range2))
        print(f"Random number between {in_range} and {in_range2}: {randomNumber}")
        
    except ValueError:
        print("Please enter valid integers")

get_random_number()
