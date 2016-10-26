while True:
    try:
        num_a = int(input("Enter a number (or a letter to exit)"))
        operator = input("Enter an operation!")
        num_b = int(input("Enter another number!"))
    except:
        break
    
    if operator == "+":
        print("%s:  %d" % ("Result", num_a + num_b))

    if operator == "-":
        print("%s:  %d" % ("Result", num_a - num_b))

    if operator == "/":
        print("%s:  %d" % ("Result", num_a / num_b))
    
    if operator == "*":
        print("%s:  %d" % ("Result", num_a * num_b))
