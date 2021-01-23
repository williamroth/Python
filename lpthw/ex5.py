name = 'Will Roth'
age = 39 # :(
height = 72 # inches
weight = 178 # due to quarentine, not really
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'
weight_in_kg = float(weight) / 2.2046
height_in_cm = float(height) * 2.54

print "Let's talk about %s." % name
# print(f"Let's talk about {name}") only works in python 3.6 and higher
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that is healthy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#tricky line
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#converted height and weight to kg and cm
print "Weight in kg is %55s" % int(round(weight_in_kg))
print "Height in cm is %55s" % int(round(height_in_cm))
