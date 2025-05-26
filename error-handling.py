while True:
    try:
        num1 = float(input("Enter the number you are trying to divide: "))
        num2 = float(input("Enter the divisor: "))
        
        result = num1/num2
        
    except ValueError:
        print("Please enter a valid numerical value")
        
    except ZeroDivisionError:
        print("You cannot divide a number by zero, please try again")
        
    else:
        print(f"The result of {num1} divided by {num2} is: {result}")
        