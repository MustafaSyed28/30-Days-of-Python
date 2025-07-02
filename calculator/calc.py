while True:
    try:
        num1 = float(input("Please enter a number:"))
        num2 = float(input("Please enter another number: "))

        operator = input("Please enter the operator (+, -, *, /): ")        

        if operator == "+":
            calculation = num1 + num2
            entry = ("{} + {} = {}".format(num1,num2,calculation))  
            print(entry) 

        elif operator == "-":
            calculation = num1 - num2
            entry = ("{} - {} = {}".format(num1,num2,calculation)) 
            print(entry)

        elif operator == "*":
            calculation = num1 * num2
            entry = ("{} * {} = {}".format(num1,num2, calculation)) 
            print(entry)   

        elif operator == "/":
            calculation = num1 / num2
            entry = ("{} / {} = {}".format(num1, num2, calculation))
            print(entry)

        else:   
            print("You have not entered a valid operator, please try again.")
            continue

        choice = input("Continue - Y / No - N: ")
        if choice == "N":
            break

    except ValueError:
        print("Wrong key entered. Please key in a number")

    except ZeroDivisionError:
        print("You cannot divide by zero. Please try again!") 


        