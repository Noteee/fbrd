import random
attck=0
while not int(attck) in range(1,4):
    try:
        attck=int(input("Adja meg a támadók számát! (1-3)  : "))
    except:
        print('Ez nem szám!')
deffse=0
while not int(deffse) in range(1,3):
    try:
        deffse=int(input("Adja meg a védők számát! (1-2)  : "))
    except:
        print('Ez nem szám!')

if (attck==3) & (deffse==2):
    attacker=[random.randrange(1,6),random.randrange(1,6),random.randrange(1,6)]
    defender=[random.randrange(1,6),random.randrange(1,6)]
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    print("%s:   %d - %d - %d" % ("Attacker",attacker[0],attacker[1],attacker[2]))
    print("%s:   %d - %d"  % ("Defender",defender[0],defender[1]))

    if (attacker[0]>defender[0]) & (attacker[1]>defender[1]):
        print('Defender: lost 2 unit')
    elif (attacker[0]<defender[0]) &  (attacker[1]<defender[1]):
        print('Attacker: lost 2 unit')
    elif (attacker[0]<defender[0]) &  (attacker[1]>defender[1]):
        print('Attacker: lost 1 unit')
        print('Defender: lost 1 unit')    
    elif (attacker[0]>defender[0]) &  (attacker[1]<defender[1]):
        print('Attacker: lost 1 unit')
        print('Defender: lost 1 unit')    
    elif (attacker[0]==defender[0]) &  (attacker[1]<defender[1]):
        print('Attacker: lost 2 unit')
    elif (attacker[0]==defender[0]) &  (attacker[1]>defender[1]):
        print('Attacker: lost 1 unit')
        print('Defender: lost 1 unit')
    elif (attacker[0]<defender[0]) &  (attacker[1]==defender[1]):
        print('Attacker: lost 2 unit')        
    elif (attacker[0]>defender[0]) &  (attacker[1]==defender[1]):
        print('Defender: lost 1 unit')    
        print('Attacker: lost 1 unit')
    elif (attacker[0]==defender[0]) &  (attacker[1]==defender[1]):
        print('Attacker: lost 2 unit')

elif (attck==2) & (deffse==2):
    attacker=[random.randrange(1,6),random.randrange(1,6)]
    defender=[random.randrange(1,6),random.randrange(1,6)]
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    print("%s:   %d - %d " % ("Attacker",attacker[0],attacker[1]))
    print("%s:   %d - %d"  % ("Defender",defender[0],defender[1]))

    if (attacker[0]>defender[0]) & (attacker[1]>defender[1]):
        print('Defender: lost 2 unit')
    elif (attacker[0]<defender[0]) &  (attacker[1]<defender[1]):
        print('Attacker: lost 2 unit')
    elif (attacker[0]<defender[0]) &  (attacker[1]>defender[1]):
        print('Attacker: lost 1 unit')
        print('Defender: lost 1 unit')    
    elif (attacker[0]>defender[0]) &  (attacker[1]<defender[1]):
        print('Attacker: lost 1 unit')
        print('Defender: lost 1 unit')    
    elif (attacker[0]==defender[0]) &  (attacker[1]<defender[1]):
        print('Attacker: lost 2 unit')
    elif (attacker[0]==defender[0]) &  (attacker[1]>defender[1]):
        print('Attacker: lost 1 unit')
        print('Defender: lost 1 unit')
    elif (attacker[0]<defender[0]) &  (attacker[1]==defender[1]):
        print('Attacker: lost 2 unit')        
    elif (attacker[0]>defender[0]) &  (attacker[1]==defender[1]):
        print('Defender: lost 1 unit')    
        print('Attacker: lost 1 unit')
    elif (attacker[0]==defender[0]) &  (attacker[1]==defender[1]):
        print('Attacker: lost 2 unit')

elif (attck==1) & (deffse==2):
    attacker=[random.randrange(1,6)]
    defender=[random.randrange(1,6),random.randrange(1,6)]
    defender.sort(reverse=True)
    print("%s:   %d" % ("Attacker",attacker[0]))
    print("%s:   %d - %d"  % ("Defender",defender[0],defender[1]))

    if attacker[0]>defender[0]:
        print('Defender: lost 1 unit')
    elif attacker[0]==defender[0]:
        print('Attacker: lost 1 unit')
    elif attacker[0]<defender[0]:
        print('Attacker: lost 1 unit')

elif (attck==2) & (deffse==1):
    attacker=[random.randrange(1,6),random.randrange(1,6)]
    defender=[random.randrange(1,6)]
    attacker.sort(reverse=True)
    print("%s:   %d - %d " % ("Attacker",attacker[0],attacker[1]))
    print("%s:   %d"  % ("Defender",defender[0]))

    if attacker[0]>defender[0]:
        print('Defender: lost 1 unit')
    elif attacker[0]==defender[0]:
        print('Attacker: lost 1 unit')
    elif attacker[0]<defender[0]:
        print('Attacker: lost 1 unit')

elif (attck==1) & (deffse==1):
    attacker=[random.randrange(1,6)]
    defender=[random.randrange(1,6)]
    print("%s:   %d" % ("Attacker",attacker[0]))
    print("%s:   %d" % ("Defender",defender[0]))

    if attacker[0]>defender[0]:
        print('Defender: lost 1 unit')
    elif attacker[0]==defender[0]:
        print('Attacker: lost 1 unit')
    elif attacker[0]<defender[0]:
        print('Attacker: lost 1 unit')


