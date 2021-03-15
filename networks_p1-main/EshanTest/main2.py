import string
import time
import Options_SmartHome as Op
import classes
#import shserver as server
#import shclient as client

clAuth = classes.Authentication()

# User session
def session():
    print("Welcome to your Smart Home" )
    clAuth.login()
    '''print(
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
            print("Light color is " + str(opt) + ", lights dimmed to " + str(optn) + "%")'''


def main():
    session()
    

if __name__ == "__main__":
    main()