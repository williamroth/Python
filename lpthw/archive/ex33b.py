
# collect the numbers from the user to apply below
low_num = raw_input("Give me a low number: ")
high_num = raw_input("Give me a high_number: ")
incriment = raw_input("Give me an incriment: ")

#establishing a blank list to start
number_list = []

# converting string
num = int(low_num)
incriment = int(incriment)

# it took a while for me to understand that I needed the incriment
# as a third argument "If the step argument is omitted, it defaults to 1."
for num in range(low_num), int(high_num), incriment):
    print "At the top of num is %d" % num

    number_list.append(num)
    print "The number list: ", number_list

    num = num + incriment
    print "At the bottom of num is %d" % num

print "\nDone!"
