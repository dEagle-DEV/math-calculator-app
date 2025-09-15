import math_module

bot_name: str = 'Ted'  # Bot name

while True:  # Loop initiation with a Boolean
    user_input: str = input("You: ").lower()  # Prompting user to enter input and normalizing to lower
    if user_input in ["hello", "hi", "greetings", "hey"]:  # If statement containing a list of 3 strings
        print(f"{bot_name}: Hello and welcome to the Math Wizard!")
        print("Please type 'help', '/help' or 'info' for more information")

    elif user_input in ["+", "add"]:  # Else if user enters any of the 2 strings + or add
        print(f"{bot_name}: Sure, let's do some Math")  # We print this
        num1, num2 = math_module.get_two_numbers(
            f"{bot_name}: Type two numbers separated by a space: ")  # Creating the variable math_input which results from the print function
        result = math_module.add_numbers(num1, num2)
        print(f"{bot_name}: The result is {result}")

    elif user_input in ["multiply", "*"]:
        print(f"{bot_name}: Let´s multiply then!")
        num1, num2 = math_module.get_two_numbers(f"{bot_name}: Type two numbers separated by a space: ")
        result = math_module.multiply_numbers(num1, num2)
        print(f"The result is {result}")

    elif user_input in ["-", "subtract"]:
        print(f"{bot_name}: Let's subtract then")
        num1, num2 = math_module.get_two_numbers(f"{bot_name}: Please enter two numbers separated by a space")
        result = math_module.subtract_numbers(num1, num2)
        print(f"{bot_name:} The result is {result}")


    elif user_input in ["divide", "/"]:
        print("Let's divide then!")
        num1, num2 = math_module.get_two_numbers(f"{bot_name}: Please enter two numbers separated by a space")
        result = math_module.divide_numbers(num1, num2)
        print(f"The result is {result}")


    elif user_input in ["power"]:
        print("Let's exponentiate then!")
        num1, num2 = math_module.get_two_numbers(f"{bot_name}: Please enter two numbers separated by a space")
        result = math_module.power_numbers(num1, num2)
        print(f"{bot_name}: The result is {result}")


    elif user_input in ["square root"]:
        print("Let's calculate Square roots")
        num1 = math_module.get_one_number(f"{bot_name}: Please enter the number you wish to calculate for")
        result = math_module.square_root(num1)
        print(f"{bot_name} The result is {result}")

    elif user_input in ["modulus"]:
        print(f"{bot_name}: Let's calculate Modulus!")
        num1, num2 = math_module.get_two_numbers(f"{bot_name}: Please enter two numbers separated by a space")
        result = math_module.modulus(num1, num2)
        print(f"{bot_name}: The result is {result}")

    elif user_input in ["thank you", "thanks"]:
        print(f"{bot_name}: My pleasure! Type 'exit' when you are done!")
        print("However, if you wish to continue, simply type a new operator")

    elif user_input in ["exit", "bye", "see you"]:  # If statement with exit logic
        print(f"{bot_name}: Goodbye! Have a wonderful day")  # Print of bye message
        break  # Closes loop

    elif user_input in ["help", "info", "/help"]:
        print("Type 'add' or '+' to proceed with a sum.")
        print("Type 'multiply' or '*' to proceed with a multiplication.")
        print("Type 'subtract' or '-' to proceed with a subtraction.")
        print("Type 'divide' or '/' to proceed with a division.")
        print("Type 'power' to proceed with an Exponentiation")
        print("Type 'Square Root' to proceed with Square Roots ")
        print("Type 'Modulus' to proceed with Modulus")

    else:
        print(
            f"{bot_name}: Sorry, I do not understand you. Please type '/help' for help.")  # For any other condition we print this
