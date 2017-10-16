def awesome_sauce():
    for value in range(1,101):
        if value % 2 == 0 and value % 7 == 0:
            print "awesomesauce!"
        elif value % 2 == 0:
            print "awesome"
        elif value % 7 == 0:
            print "sauce"
        else:
            print value

awesome_sauce()
