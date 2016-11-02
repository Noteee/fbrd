doors = [False] * 100

#cycles thru the 100 door and toggles it between True and False
for i in range (100):
    for j in range (i, 100, i+1):
        doors[j] = not doors[j]

#prints out the index and the value of the doors, if its true it prints open if not it prints closed
for k, door in enumerate(doors, start=1):
    print("Door %d is" % (k), "open" if door else "closed")