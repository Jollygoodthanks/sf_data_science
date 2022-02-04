""" Guess the number"""

import numpy as np

number = np.random.randint(1, 101)  #think about the number

#number of times to try
count = 0

while True:
    count+=1
    predict_number = int(input("Guess the number from 1 to 100: "))

    if predict_number > number:
        print("The number should be smaller!")

    elif predict_number < number:
        print("The number should be bigger!")

    else:
        print(f"You guessed the number! This number = {number}, with {count} tries")
        break #stop the game, leave the loop

