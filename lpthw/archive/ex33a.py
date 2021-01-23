def number_list(low_number, high_number, incriment):
    num = low_number
    list = []
    while num < high_number:

        print "At the top of 'num' is %d" % num
        list.append(num)

        num += incriment

        print "Numbers now: ", list
        print "At the bottom 'num' is %d\n" % num

# low_number = raw_input("Give a low number: ")
# high_number = raw_input("Now give a high number: ")

low_number, high_number = raw_input("Give a low and high number: ").split()
incriment = raw_input("How many number should we skip each time? ")

low_number = int(low_number)
high_number = int(high_number)
incriment = int(incriment)

number_list(low_number, high_number, incriment)
