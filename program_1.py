# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

#Tanner Rosenthal
#3/26/25
#Name File Counter
def count_file_lines():

    with open('names.txt', 'r') as file:
        names = file.readlines()

    names_count = 0
    for name in names:
        names_count +=1
    file.close()
    print(names_count)
    
# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
