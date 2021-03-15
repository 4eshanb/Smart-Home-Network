import time
# All accounts
users = {}

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

class Authentication:
    # Form validation
    def validate(self, form):
        if len(form) > 0:
            return False
        return True

    # Login authorization
    def loginauth(self, username, password):
        if username in users:
            if password == users[username]["password"]:
                print("Login successful")
                return True
        return False

    # Login
    def login(self):
        print('Register or Login?')
        inp = input()
        if inp == 'register' or inp == "Register":
            self.register()
        
        while True:
            username = input("Username: ")
            if not len(username) > 0:
                print("Username can't be blank")
            else:
                break
        while True:
            password = input("Password: ")
            if not len(password) > 0:
                print("Password can't be blank")
            else:
                break

        if self.loginauth(username, password):
            return session(username)
        else:
            print("Invalid username or password\n")
            self.register()

    # Register
    def register(self):
        print("Please create a new account\n")
        while True:
            username = input("New username: ")
            if len(username) == 0:
                print("Username Invalid")
                continue
            else:
                break
    
        while True:
            password = input("New password: ")
            if len(password) == 0:
                print("Password can't be blank")
                continue
            else:
                break
        print("Creating account...")
        users[username] = password
        print(users)
        time.sleep(1)
        print("Account has been created")
