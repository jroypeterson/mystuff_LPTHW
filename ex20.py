from sys import argv #importing the argv module so that you can call an external thing

script, input_file = argv #tellilng us that input_file will be the external file used in the script

def print_all(f):    #new function that reads a variables
    print f.read()   # .read() reads the whole document

def rewind(f):  #new function that resets the place to read to beg. of the file
    f.seek(0)   # variable.seek function says what line to go to

def print_a_line(line_count, f): #new function that prints a single line
    print line_count, f.readline() #readline function called

current_file = open(input_file) #program begins here. Opens the file.

current_file.seek(16)
print current_file.read()
'''
print "First let's print the whole file:\n"

print_all(current_file) #prints the whole uploaded file

print "Now let's rewind, kind of like a tape."

rewind(current_file) # returns the file reader to the beginning of the file

print "Let's print three lines:"

current_line = 1  # starting to print each line succesively. it just
print_a_line(current_line, current_file) # this doesn't actually tell the program what line to print.
# It just prints from where it ended
current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)
'''
