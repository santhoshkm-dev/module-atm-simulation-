class Withdrawal:
    def __init__(self, account):
        self.account = account

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))

            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > self.account.balance:
                print("Insufficient balance.")
            else:
                self.account.balance -= amount
                print(f"Successfully withdrawn ${amount}. New balance: ${self.account.balance}")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
