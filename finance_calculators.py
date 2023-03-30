"""PROJECT BRIEFING: 
The user should be allowed to choose which calculation they want to do.
How the user capitalises their selection should not affect how the
program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’,
‘INVESTMENT’, etc., should all be recognised as valid entries. If the user
doesn’t type in a valid input, show an appropriate error message.
If the user selects ‘investment’, do the following:
● Ask the user to input:
○ The amount of money that they are depositing.
○ The interest rate (as a percentage). Only the number of the interest
rate should be entered — don’t worry about having to deal with the
added ‘%’, e.g. The user should enter 8 and not 8%.
○ The number of years they plan on investing.
○ Then ask the user to input if they want “simple” or “compound”
interest, and store this in a variable called interest. Depending on
whether or not they typed “simple” or “compound”, output the
appropriate amount that they will get back after the given period,
at the specified interest rate.
If the user selects ‘bond’, do the following:
● Ask the user to input:
○ The present value of the house. e.g. 100000
○ The interest rate. e.g. 7
○ The number of months they plan to take to repay the bond. e.g. 120
○ Calculate how much money the user will have to repay each month
and output the answer."""


# import mathmatical functions.
import math

# Provide user the message introducing them to the programme and ask them to 
# confirm which financial product they have.
print("investment\t- to calculate the amount of interest you'll earn on your investment\nbond\t\t- to calculate the amount you'll have to pay on a home loan\n\nEnter either 'investment' or 'bond' from the menu above to proceed:")
financial_product = input("Do you have an investment or a bond? ").capitalize()

""" Standardise case of financial_product variable. Check if user has bond or investment
if not, provide user with warning message that entry isn't appropriate and ask
them to try again."""
while financial_product != "Bond" and financial_product != "Investment":
    print("Your entry is not recognised. Please try again.") 
    financial_product = input("Do you have an investment or a bond? ").capitalize()

""" If user has an investment, ask them to provide value of investment, interest rate
number of years of investment and interest type. Check that interest rate is between
0 and 100, investment is more than £1, investment is for a minimum of 1 year and interest
type is compound or simple and if not, ask user to try again."""
if financial_product == "Investment":
    initial_investment = int(input("What is the value of your intended investment in £? "))
    while initial_investment <= 0:
        print("You must invest more than £0. Please try again.")
        initial_investment = int(input("What is the value of your intended investment in £? "))
    interest_rate = float(input("What interest rate have you been offered, in %? "))
    while interest_rate <= 0 or interest_rate > 100:
        print("The interest rate must be between 0 and 100%. Please try again.")
        interest_rate = float(input("What interest rate have you been offered, in %? "))
    investment_years = float(input("For how many years do you intend to hold this investment? "))
    while investment_years <= 0:
        print("You must invest for more than 0 years. Please try again.")
        investment_years = float(input("For how many years do you intend to hold this investment? "))
    interest = input("Please specify whether you want simple or compound interest: "). capitalize()
    while interest != "Simple" and interest != "Compound":
        print("Your entry is not recognised. Please try again.") 
        interest = input("Please specify whether you want simple or compound interest: "). capitalize()

    # Calculate value of return based on whether the user has selected simple or compound. Print message for user.
    # Format get_variable to 2 decimal places - instructions found at https://www.javatpoint.com/how-to-get-2-decimal-places-in-python
    if interest == "Simple":
        get_back = format((initial_investment * (1 + (interest_rate/100) * investment_years)), ".2f")
        print(f"When investing £{initial_investment} for {investment_years} year(s) at an simple interest rate of {interest_rate}% you will get back £{get_back} at the end of the investment period.")
    else:
        get_back = format(initial_investment * math.pow((1 + interest_rate/100), investment_years), ".2f")
        print(f"When investing £{initial_investment} for {investment_years} year(s) at a compound interest rate of {interest_rate}% you will get back £{get_back} at the end of the investment period.")

""" If user has a bond, ask them to provide the house value, interest rate and the number of months
for repayment. Check that the house value is more than £0, the interest rate is between 0 and 100 and the
investment is for a minimum of 1 month. If not, ask user to try again."""
if financial_product == "Bond":
    house_value = int(input("What is the current value of your house is £? "))
    while house_value <= 0:
        print("Your house must be valued at more than £0. Please try again.")
        house_value = int(input("What is the current value of your house is £? "))
    interest_rate_annual = float(input("What interest rate have you been offered, in %? "))
    while interest_rate_annual <= 0 or interest_rate_annual > 100:
        print("The interest rate must be between 0 and 100%. Please try again.")
        interest_rate_annual = int(input("What interest rate have you been offered, in %? "))
    investment_months = int(input("Over how many months do you intend to make the repayment? "))
    while investment_months <= 0:
        print("Your repayment period must be more than 0 months. Please try again.")
        investment_months = float(input("Over how many months do you intend to make the repayment? "))
    
    # Calculate monthly interest rate and value of the monthly repayment. Print message for user. 
    interest_rate_monthly = (interest_rate_annual / 12) / 100
    repayment = format((interest_rate_monthly * house_value) / (1 - (1 + interest_rate_monthly)**(-investment_months)), ".2f")
    print(f"For a bond on a house valued at £{house_value} at an annual interest rate of {interest_rate_annual}% and making repayments over a period of {investment_months} months; your monthly repayment will be £{repayment}.")