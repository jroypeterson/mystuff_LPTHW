# variable with a string
x = "There are %d types of people." % 10
#variable with a string
binary = 'binary'
#variable with a string
do_not = "don't"
#variable with a string and
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
#string inside a string here x2
print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# string inside a string above and below
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e
