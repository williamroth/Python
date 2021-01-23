print(x) #FUNCTION that's purpose is to display things for the user, x is an argument

"x" or 'x' #STRING everything inside single and double quotes is interpretted as text, except for escapes like \n \t

#stores a multi line string
'''
line1
line2
line3
'''

, # can be used to form a list or can be used to continue printing on same line

# <--- That is a POUND and it's so that the computer knows this is a comment in python

#ARITHMATIC OPERATORS
+ #addition 1 + 2
- #subtraction 2 - 1
* #multiplication 2 * 2
/ #division 6 / 2
% #modulus returns the remainder 10 % 4 value is 2
** #epxonent 2 ** 3 == 2 * 2 * 2 (true)

#COMPARISON OPERATORS
< #less-than returns True or False boolean
> #greater-than returns True or False boolean
<= #less-than-or-equal-to returns True or False boolean
>= #greater-than-or-equal-to returns True or False boolean
== #equals returns True or False boolean
!= #does-not-equal returns True or False boolean

#ASSIGNMENT OPERATORS
= # assigns right side value to left side, x = 1
+= # adds value of right side to left side, x += 1 (now equals 2)
-= # removes value of right side from left side x -= 1 (now equals 1 again)

#ARGUMENT SPECIFIERS
#ex.
print "This string: %s, This integer: %d, This float: %f" % ("hello", 4, 10.2)
print "This is a representation (repr): %r" % ("Hello")
%s #calls the first argument in the tuple, the string
%d #calls the second argment in the tuple, the integer
%f #calls the third argument in the tuple, the float
%r #calls the entire representation of a statement, useful for debugging

str(x) # converts argument x into string
int(x) # converts argument x into integer
float(x) # converts argumnet x into string
round(x) # returns to the nearest whole number of x, up or down, as a float.

#BOOLEANS
#A BOOLEAN is a value of True or False that can be fead to or returned from a a function/expression.
True
False

#INTEGERS
1 #integers are a value that can be used directly in the script like a str or boolean
2
100000

#ESCAPES
print "\n" # \n denotes a new line
print "\a" # plays the ascii bell "ding!"
print "\t" # acts as a tab
print "\uxxxx" # prints a 16-bit unicode hex value
print "\r" # carriage return (returns cursor to beginning of the line)
print "\\" # backslash will escape things like \" \' or \\ to print character as part of the string

raw_input() # function that asks user for data, usually as a keyboard response
#example
name = raw_input("What's your name?")
print "hi %s" % name
#or
print "What's your name?"
name = raw_input()
print "Hi", name

#If the condition like "2 == 2" is TRUE, do what is indented, if the condition is FALSE like "2 == 3", do not do what is indented and move on.
if condition:
    pass
elif second_condition: #if this is TRUE then pass/run, if its FALSE move on
    pass
elif third_condition:
    pass
else: #if none of the above are TRUE run the indented
    pass

#MODULES & ARGUMENTS
from module import argument #from another script, grab this part of it.

sys #python runtime system MODULE which provides functions to use
from sys import argv #function for command line arguments from user in console

script, arg1, arg2 = argv #asks user for two argments when running the script

os #operating system modules which provides functions to use
from os.path import exists # Tests whether a file path exists, returns TRUE or FALSE

math #Math module that provides functions to use

#FILE METHODS
open(x) #Opens file x
open(x, 'r') #Opens file x in READ mode, user cannot manipulate file
open(x, 'w') #Opens file in WRITE mode, can override text CAUTION!
open(x, 'a') #Opens file in APPEND mode, user can only add to bottom of file
read(x) #Reads and stores entire contents of file print x.read() prints entire file
readline(x) #Reads and stores current line in text
seek(x) #Moves cursor in file x number of bytes forward or backward
y.write(x) #Writes value from x into file y
close(x) #Closes the file, dumps it from memory

def funtion_name(arg): #Creates a function, the function has an argument requirement, when the function is called, it passes the miniscript
    miniscript

def function_name(*args): #Allows for an arbitrary number of args (a Tuple) to be input into the function.
    miniscript

def f(x):
    return y + z #stores the value of the expression if present, or else NONE is stored

; #Allows you to compound statements onto one line. But why would you want to?
