class Login:
    def __init__(self):
        self.username = "admin"
        self.password = "password123"
    
    def authenticate(self):
        try:
            attempt = 3
            while attempt > 0:
                username = input("Enter a username: ")
                password = input("Enter a password: ")

                if username == self.username and password == self.password:
                    print("Successfully logged in")
                    return True

                attempt -= 1
                if attempt > 0:
                    print(f"Invalid username or password, please try again. Attempts left: {attempt}")
                else:
                    print("Too many invalid attempts.")

        except Exception as e:
            print(f"An error occurred: {e}")

        return False
