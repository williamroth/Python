# from the sys module we are bringing in the argv command line argument
from sys import argv
# we are asking argv to ask for filename
# next to the script that we are launching from the command line
script, filename = argv
# asking the user if its ok to delete 'truncate'
# the entire contents of the file
print "We're going to erase %r." % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# prompts the user to take action on the above question
raw_input("?")
# python opens the file and stores its contents in the variable "target"
print "Opening the file..."
target = open(filename, 'w')
# deletes 'truncates' the contents of target variable
print "Truncating the file. Goodbye!"
# target.truncate()
# asks the user to add three new strings to add to the file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# tells the user that the three strings will now be written to the file
print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write("%r\n%r\n%r\n" % (line1, line2, line3))

# closes the file
print "And finally, we close it."
target.close()
