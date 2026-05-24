class Balance:

    def __init__(self):
        self.balance = 1000.00

    def check(self):
        print(f"Your Current Balance is: ${self.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: "))

            if amount > 0:
                self.balance += amount     
                print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
            else:
                print("Deposit amount must be positive.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")    
               
