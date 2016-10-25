tomb=list()
felsohat=int(input("Hányat irjak ki?"))
for i in range(0, felsohat):
    if(i==0):
        tomb.insert(0, 0)
    elif(i==1):
        tomb.insert(1, 1)
    else:
        tomb.insert(i, tomb[i-1]+tomb[i-2])
    print('{0:<3d}: {1:>30d}'.format(i+1, tomb[i]))
    
