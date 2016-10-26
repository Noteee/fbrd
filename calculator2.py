while True:
    try:
        num_a = float(input("Enter a number (or a letter to exit):   "))
                                                                #Bekéri az első számot és float-á alakítja ha tudja
        operator = input("Enter an operation!:   "   )
                                                                #Bekéri az operátort
        num_b = float(input("Enter another number:   "))
                                                                #Bekéri a második számot és floattá alakítja ha tudja
    except:
        break
                                                                #Mivel csak a számokat tudja floattá alakítani, 
                                                                #ha nem szám akkor hibának veszi ilyenkor kilép a ciklusból
    
    if (operator != "+") | (operator != "-") | (operator != "/") | (operator != "*"):
                                                                #csak akkor fussunk bele ha megfelelő az operátor
            if operator == "+":
                print("%s:  %.2f" % ("Result", num_a + num_b))

            elif operator == "-":
                print("%s:  %.2f" % ("Result", num_a - num_b))

            elif operator == "/":
                print("%s:  %.2f" % ("Result", num_a / num_b))

            elif operator == "*":
                print("%s:  %.2f" % ("Result", num_a * num_b))
                                                                #Különböző esetek lekezelése 

    print('Operators can be: + or - or / or *')
                                                                #megfelelő operátorok kiíratása
                
            

print('Leaving Calculator')
                                                                #kilépés kiíratása
