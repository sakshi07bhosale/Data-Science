
while True:
    choice = int(input("Enter your choice (1-4): "))
    a = float(input("Enter first number: ")) 
    b = float(input("Enter second number: "))
    
    match choice:
        case 1:
            print("Result:", a + b)

        case 2:
            print("Result:", a - b)

        case 3:
            print("Result:", a * b)
           

        case 4:
            try:
                print("Result:", a/b)
            except:
                print("ZeroDivisionError: division by zero")


        case _:
            print("Invalid choice! Please enter 1 to 4.")
            break