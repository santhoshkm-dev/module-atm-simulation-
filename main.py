import login
import balance
import withdrawal


user_login = login.Login()
user_balance = balance.Balance()
user_withdrawal = withdrawal.Withdrawal(user_balance)

is_logged_in = user_login.authenticate()

if is_logged_in:
    print("Welcome to ATM")

    while True:
        print("\nChoose an option:")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        option = input("Enter option: ")

        if option == "1":
            user_balance.check()

        elif option == "2":
            user_balance.deposit()

        elif option == "3":
            user_withdrawal.withdraw()

        elif option == "4":
            print("Thank you. Visit again.")
            break

        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")

else:
    print("Login failed.")
