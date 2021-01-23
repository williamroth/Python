# Allows the user to input while executing the script
from sys import argv
# Designates that the filename will be required when executing the script
script, filename = argv
# Loads the contents of the filename into txt
txt = open(filename)
# Returns the text to the user in the console
print "Here is your file %r:" % filename
print txt.read()

# asks the user for the filename again and loads it into file_again
print "Type the filename again:"
file_again = raw_input("> ")
# loads the contents of the file_again into txt_again
txt_again = open(file_again)
# Returns the txt_again which is the original file to the console for the user
print txt_again.read()
txt.close()
txt_again.close()
