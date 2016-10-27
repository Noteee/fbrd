import sys

# This function determines the number of cmdl agruments and returns these arguments as
#a title type string, if theres no arguments other than the file name it returns "World" 
def argname ():
    if len(sys.argv)==1:
        return "World"
    elif len(sys.argv) ==2:
        return sys.argv[(len(sys.argv)-1)].title()
    elif len(sys.argv) ==3:
        return sys.argv[(len(sys.argv)-2)].title() + " " + sys.argv[(len(sys.argv)-1)].title()
    else:
        return "World"
    
#prints out the "Hello" string and the argname-return-value and a "!""
print("%s %s%s " % ("Hello", argname(), "!"))







