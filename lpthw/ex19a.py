from sys import argv
script, din, show, dish = argv

def evening(dinner, tv_show, dishes):
    print "First we make %s." % dinner
    print "Then we watch %s." % tv_show
    print "Finally we wash %s.\n" % dishes

#1 direct input
print "Last evening:"
evening("empanadas and cole slaw", "Ted Lasso", "plates, forks, and a pan")

best_dinner = "steak and wine"
best_tv_show = "Avatar"
best_dishes = "nothing"

#2 variable input
print "Best evening:"
evening(best_dinner, best_tv_show, best_dishes)

#3 user input
q_dinner = raw_input("What do you want for dinner? ")
q_tv_show = raw_input("What show will you watch? ")
print "What dishes will it take to make", q_dinner, "?",
q_dishes = raw_input()

print "\nOk, here is your evening plan:"
evening(q_dinner, q_tv_show, q_dishes)

#4 argv input
evening(din, show, dish)

#5 combine a few different
print "Here is a list of your dinner plans:"
print best_dinner, ",", q_dinner, ",", din
