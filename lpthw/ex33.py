i = 0
numbers = []

while i < 6:
    print "At the top of i is %d" % i
    numbers.append(i)

    i = i + 1 #can't we just use 'i += 1' ?
    print "Numbers now: ", numbers
    print "At the bottom i is %d\n" % i

print "The numbers: "

for num in numbers:
    print num
