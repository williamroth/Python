# Creating funtion c&c that tells user how many cheese and crackers they have
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# feeding number arguments directly to the c&c function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# creating a variable to feed into cheese_count and boxes_of_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# feeding the variables from above into c&c function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Doing math for the arguments for the c&c funtion
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# showing that we can combine variables and math for the arguments
print "And we can combine the two, varbiables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
