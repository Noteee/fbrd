import sys


# This function determines the number of cmdl agruments and returns these arguments as
#a title type string, if theres no arguments other than the file name it returns "World" 
def argname ():
    lenght = len(sys.argv)
    if lenght == 1:
        return "World"
    elif lenght == 2:
        return sys.argv[(lenght-1)].title()
    elif lenght == 3:
        return sys.argv[(lenght-2)].title() + " " + sys.argv[(lenght-1)].title()
    else:
        return "World"
    

#prints out the "Hello" string and the argname-return-value and a "!""
print("%s %s%s " % ("Hello", argname(), "!"))