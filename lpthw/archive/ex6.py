#assigning value to my variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#printing two full sentences using the variables above
print x
print y

# reitterating and demonstrating use of %r and %s
print "I said: %r." % x
print "I also said: '%s'." % y

#assigning false to the variable hilarious
hilarious = False

# %r comes into play when printing below
joke_evaluation = "Isn't that joke so funny!? %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
