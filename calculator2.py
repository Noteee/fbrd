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
        #Mivel a bekérés számot vár így ha nem azt kap azt hibának veszi ilyenkor kilép a ciklusból
    
    if (operator != "+") | (operator != "-") | (operator != "/") | (operator != "*"):
        
            if operator == "+":
                print("%s:  %.2f" % ("Result", num_a + num_b))

            elif operator == "-":
                print("%s:  %.2f" % ("Result", num_a - num_b))

            elif operator == "/":
                print("%s:  %.2f" % ("Result", num_a / num_b))

            elif operator == "*":
                print("%s:  %.2f" % ("Result", num_a * num_b))

    
    print('Operators can be: + or - or / or *')
        
                
            #Különböző esetek lekezelése ^

print('Leaving Calculator')
