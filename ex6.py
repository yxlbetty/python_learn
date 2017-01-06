
x = "There are %d type of people" % 10 # 字符串赋值给x
binary = "binary" # 字符串赋值给 binary
do_not ="don't" # 字符串赋值
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "isn't that joke so funny?! % r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
