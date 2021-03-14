import time
# All accounts
users = {
    "root": {
        "password": "password",
        "group": "admin"
        # "SmartObj": [Lights, Alarm, Lock, Thermostat, SecCam, AutoBlind]
    }
}

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

class Authentication:
    # Form validation
    def validate(form):
        if len(form) > 0:
            return False
        return True

    # Login authorization
    def loginauth(username, password):
        if username in users:
            if password == users[username]["password"]:
                print("Login successful")
                return True
        return False

    # Login
    def login():
        while True:
            username = "root"  # input("Username: ")
            if not len(username) > 0:
                print("Username can't be blank")
            else:
                break
        while True:
            password = "Ligma"  # input("Password: ")
            if not len(password) > 0:
                print("Password can't be blank")
            else:
                break

        if loginauth(username, password):
            return session(username)
        else:
            print("Invalid username or password")

    # Register
    def register():
        while True:
            username = input("New username: ")
            if not len(username) > 0:
                print("Username can't be blank")
                continue
            else:
                print("Username Invalid")
                break
        while True:
            password = input("New password: ")
            if not len(password) > 0:
                print("Password can't be blank")
                continue
            else:
                break
        print("Creating account...")
        users[username] = {}
        users[username]["password"] = password
        users[username]["group"] = "user"
        # users[username]["SmartObj"] = [] #User decides which smart objects they have
        time.sleep(1)
        print("Account has been created")
