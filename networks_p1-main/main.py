# Import modules
import string
import time
import Options_SmartHome as Op
import classes

OpAlarm = Op.Alarm
OpLights = Op.Lights(5, 'blue')
OpLocks = Op.Locks
clAuth = classes.Authentication

# User session
def session(username):
    print("Welcome to your Smart Home " + username)
    print(
        "Options: 1. Lights | 2. Alarm | 3. Locks | 4. Security Camera | 5. Blinds | 6. logout")  # lights, alarm, locks(5), security camera, blinds
    while True:
        option1 = input(username + " > ")
        if option1 == "logout":
            print("Logging out...")
            break
        elif option1 == 1:
            opt = input("Enter desired color for light: ")
            optn = input("Enter dim level for lights (by percentage 0 - 100): ")
            light = Op.Lights(opt, optn)
            print("Light color is " + str(opt) + ", lights dimmed to " + str(optn) + "%")

'''
# On start
print("Welcome to the system. Please register or login.")
print("Options: login | register | exit")  # lights, alarm, locks(5), security camera, blinds
while True:
    option = input("> ")
    # print(option)
    if option == "login":
        clAuth.login()
    elif option == "register":
        clAuth.register()
    elif option == exit:
        break
    else:
        print("Input is not an option")
'''

print("Welcome to Smart Home. What would you like to control?")
print("Lights, Alarm, Locks")
'''
while True:
    selection = input("> ")
    if selection == "Lights":
        print("What would you like to do with the lights?")
        print("Change: color | dim")
        sel = input("> ")
        if sel == "color":
            colVal = OpLights
            print("Color is %", colVal)
        elif sel == "dim":
            dimVal = OpLights.get_dim()
            print("Dim is %", dimVal)
'''

print(OpLights.get_dim())

# On exit
print("Shutting down...")
time.sleep(1)