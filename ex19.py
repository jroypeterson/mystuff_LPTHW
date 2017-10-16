#you are defining a function that has 2 inputs. This input is printed
def cheese_and_crackers(cheese_count, box_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % box_of_crackers
    print "man that's enough for a party"
    print "Get a blanket. \n"

'''this calls the function with teh values 20 and 30'''
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#This runs the script again with different variables
print "Or, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers (amount_of_cheese, amount_of_crackers)

#THis is the 3rd call of the script with new numbers
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

'''This combines a previous variable with additon'''
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)


def cheese_and_salsa(x, salsa):
    print "You have %d cheeses!" % x
    print "You have %d boxes of salsa" % salsa

x = raw_input("How much cheese you bringin?")
x = int(x)

cheese_and_salsa(x,20)
