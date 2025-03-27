# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

#Tanner Rosenthal
#3/27/25
#File Number Reader

def sum_numbers_from_file(): 

    file_numbers = open('numbers.txt', 'r')

    try:
        total = 0
        file_contents = file_numbers.readlines()
        for line in file_contents:
            number = line.strip()
            number = int(number)
            total += number

    except IOError as e:
        print(f"An IOError occurred: {e}")
    except ValueError as e:
        print(f"A ValueError occurred: {e}")
    finally:
        file_numbers.close()
        print(f"The total of the numbers in 'numbers.txt' is {total}")


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
