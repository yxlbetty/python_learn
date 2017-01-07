from sys import argv

script, filename = argv

txt=open(filename)
print "this is content:"
print txt.read()