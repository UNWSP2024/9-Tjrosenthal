# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

#Tanner Rosenthal
#3/27/25
#Random Number File Generator

import random
file = open('number.txt', 'a')

number_amount = random.randint(0, 1000)

for number in range(0, number_amount):
    random_number = random.randint(1, 500)
    file.write(f"{random_number}\n")

file.close()

print(f"{number_amount} numbers have been written to 'number.txt'")



