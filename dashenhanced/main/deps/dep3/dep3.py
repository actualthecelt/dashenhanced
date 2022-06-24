import os
import getpass as gp

pass1 = "pass1"
pass2 = "pass2"
pass3 = "pass3"

def enter():
    print("")

print("LOGIN PAGE")
enter()
userinput = input("Username: ")
if userinput == "user1":
    passinput1 = gp.getpass("Password: ")
    if passinput1 == pass1:
        print("Access granted.")
    else:
        print("Access denied.")
elif userinput == "user2":
    passinput2 = gp.getpass("Password: ")
    if passinput2 == pass2:
        print("Access granted.")
    else:
        print("Access denied.")
elif userinput == "user3":
    passinput3 = gp.getpass("Password: ")
    if passinput3 == pass3:
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("No existing username matching given input.")