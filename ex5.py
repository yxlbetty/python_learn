
name = 'zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
i = 0.4 # pound=0.4536kg
j= weight * i

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "he's %r pounds heavy." % weight
print "he's %s kg heavy." % j
print "Actually that's not too heavy."
print "He got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "if i add %d, %d, and %d i get %d." % (age, height, weight, age + height + weight) 
