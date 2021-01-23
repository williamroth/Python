from sys import argv

script, input_file = argv
#prints out all of whatever file you pass into it
def print_all(f): #f is like an operator?
    print f.read()
#moves the cursor, if you will, to the first byte of the file you pass it
def rewind(f):
    f.seek(0)
#allows us to see where the cursor is in the file and then prints that line to the \n
def print_a_line(line_count, f):
    print line_count, f.readline(),
#opens the file we established in argv and stores it in current_file variable
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file) #runs the 'print_all' function on the open file

print "Now let's rewind, kind of like a tape."

rewind(current_file) #runs the 'rewind' function on the open file

print "Let's print three lines:"
#this line is really for the users to understand that since we ran rewind earlier,
#that we are currently on line 1.
current_line = 1
print_a_line(current_line, current_file) #runs print_a_line function

current_line += 1 #adds 1 to the current line to show user we are on line 2 of the file
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
