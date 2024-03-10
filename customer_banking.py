# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # Insert super code AVC
    # ADD YOUR CODE HERE
    savings_balance = float(input('Please enter your savings balance: '))
    savings_int = float(input('Please enter your savings interest rate: '))
    savings_maturity = int(input('Please enter the number of months for savings: '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, int_earned = create_savings_account(savings_balance, savings_int, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Savings Account: Interst Earned: {int_earned:.2f}, Updated Balance: {updated_savings_balance:.2f}')
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('Please enter your CD Account balance: '))
    cd_int = float(input('Please enter your CD Account interest rate: '))
    cd_maturity = int(input('Please enter number of monthsfor CD Account: '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, int_earned = create_cd_account(cd_balance, cd_int, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'CD Account: Interst Earned: {int_earned:.2f}, Updated Balance: {updated_cd_balance:.2f}')
if __name__ == "__main__":
    # Call the main function.
    main()