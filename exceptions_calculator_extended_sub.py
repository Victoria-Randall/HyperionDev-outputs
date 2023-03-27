import os

# Provide welcome statement and set variables.
print("Welcome to our calculator.")
equation = 0
operators = ["x", "/", "+", "-"]
user_continue = "y"
user_continue_options = ["y", "n"]
user_file_name1 = ""
user_file_name2 = ""

while user_continue == "y":
    # Ask user to provide first number. Check value is a number and if not, ask user to try again. 
    while True:
        try: 
            user_number1 = float(input("Please enter a number: "))
            break
        except ValueError:
            print("Opps! That was not a valid number. Please try again: ")

    # Ask user to provide a second number. Check value is a number and if not, ask user to try again.
    while True:
        try: 
            user_number2 = float(input("Please enter another number: "))
            break
        except ValueError:
            print("Opps! That was not a valid number. Please try again: ")

    # Ask user to confirm what operator they would like to use. If user has not provided a valid 
    # operator, ask them to try again.
    user_operator = str(input("What operation would you like to perform? Please input x for multiply, / for divide, + for addition or - for subtraction: ")).lower()
    while user_operator not in operators:
        user_operator = input("You have not provided a recognised operator. Please input x for multiply, / for divide, + for addition or - for subtraction: ").lower()

    # Check of ZeroDivisionError and if found, ask user to select another operator.
    while user_number2 == 0 and user_operator == "/":
        user_operator = input("It's not possible to divide by O. Please select another operator from x, + or -: ")

    # Perform calculations based on user inputs (to 3 decimal places) and print equation and output.
    if user_operator == "x":
        equation = format((user_number1 * user_number2), ".3f")
    elif user_operator == "/" :
        equation = format((user_number1 / user_number2), ".3f")
    if user_operator == "+" :
        equation = format((user_number1 + user_number2), ".3f")
    if user_operator == "-" :
        equation = format((user_number1 - user_number2), ".3f")

    output = f"{user_number1} {user_operator.lower()} {user_number2} = {equation}"
    print(output)

    # Save user's equation to a text file.
    with open('calculator_output.txt', 'a') as file:
        for line in str(output): 
            file.write(line)
        file.write('\n')

    # Ask user if they would like to run another calculation. Check answer is valid and
    # if not, repeat the question. If answer is y, they will restart the calculator
    # because of the while look statement at the beginning.
    user_continue = (input("Would you like to run another calculation? Please enter y for yes or n for no. ")).lower()
    while user_continue not in user_continue_options:
        user_continue = input("Sorry, but I did not recognise your answer. Would you like to run another calculation? Please enter y for yes or n for no. ").lower()

    # If user does not wish to continue, ask them to provide a file name.
    if user_continue == "n":
        user_file_name1 = input("Please provide the name for your output file: ")
    
        """ I found instructions on how to rename a text file here: 
        https://www.guru99.com/python-rename-file.html
        I don't think I've completed this last element of the programme as expected.
        Indeed, there's an error if the user selects the same file name twice but
        I'm not sure how to resolve that so further guidance would be appreciated."""
        os.rename("calculator_output.txt",str(user_file_name1))

        # Check that user has confirmed the correct file, if not ask them again.
        user_file_name2 = input("Please confirm the name of the file you would like to open: ")
        while user_file_name1 != user_file_name2:
            user_file_name2 = input("That file name was not recognised. Please confirm the name of the file you would like to open: ")

        # Open file and display the contents, i.e. all of the equations performed 
        # by the user. I found instructions here: 
        # https://stackoverflow.com/questions/30768056/importing-external-txt-file-in-python
        file = open(str(user_file_name1), 'r')
        content = file.read()
        print("You have used our calculator for the following sums: ")
        print(content)
        file.close()
        os.remove(str(user_file_name1))

