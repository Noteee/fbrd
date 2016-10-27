import sys
lenght = len(sys.argv)
if lenght == 1:
   print("Hello World!")
elif lenght == 2:
   cmdarg1 = str(sys.argv[1].title())
   print("%s %s%s " % ("Hello", cmdarg1,"!" ))
elif lenght == 3:
   cmdarg1 = str(sys.argv[1].title())
   cmdarg2 = str(sys.argv[2].title())
   print("%s %s %s%s " % ("Hello",cmdarg1, cmdarg2,"!" ))
else: 
   cmdarg1 = str(sys.argv[1].title())
   print("%s %s%s " % ("Hello", cmdarg1,"!" ))