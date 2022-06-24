import os
import getpass as gp
import subprocess
import time as t
import sqlite3 as sql
from datetime import datetime

con = sql.connect("data.db")
cur = con.cursor()
now = datetime.now()
currenttime = str(now)

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def ct():
    os.system('cls')

print("LOGIN PAGE\n\nSelect which user you want to log into.\n\n1 = User1\n2 = User2\n3 = User3\n\n")

selectuser = input("User: ")
if selectuser == "1":
    ct()
    print("LOGIN PAGE\n\nSelected user: User1")
    passinput = gp.getpass("Password:")
    statement = f"SELECT username from user1_dep1 WHERE password='{passinput}';"
    cur.execute(statement)
    if not cur.fetchone():
        ct()
        print(bcolors.FAIL + "Incorrect password." + bcolors.RESET)
        log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user1_logs.txt", "a")
        log.write("" + currenttime + " - User1 was unsuccessfully logged into. Reason: incorrect password \n")
        log.close()
    else:
        ct()
        print(bcolors.OK + "Access granted.\n" + bcolors.RESET + "Redirecting you in 3 seconds...")
        log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user1_logs.txt", "a")
        log.write("" + currenttime + " - User1 was successfully logged into \n")
        log.close()
        t.sleep(3)
        subprocess.call(r"python C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1.py 1", shell=True)
elif selectuser == "2":
    ct()
    print("LOGIN PAGE\n\nSelected user: User2")
    passinput = gp.getpass("Password:")
    statement = f"SELECT username from user2_dep1 WHERE password='{passinput}';"
    cur.execute(statement)
    if not cur.fetchone():
        ct()
        print(bcolors.FAIL + "Incorrect password." + bcolors.RESET)
        log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user1_logs.txt", "a")
        log.write("" + currenttime + " - User2 was unsuccessfully logged into. Reason: incorrect password \n")
        log.close()
    else:
        ct()
        print(bcolors.OK + "Access granted.\n" + bcolors.RESET + "Redirecting you in 3 seconds...")
        log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user2_logs.txt", "a")
        log.write("" + currenttime + " - User2 was successfully logged into \n")
        log.close()
        t.sleep(3)
        subprocess.call(r"python C:\Users\Celt\dashenhanced\main\deps\dep1\users\user2.py 1", shell=True)
elif selectuser == "3":
    ct()
    print("LOGIN PAGE\n\nSelected user: User3")
    passinput = gp.getpass("Password:")
    statement = f"SELECT username from user3_dep1 WHERE password='{passinput}';"
    cur.execute(statement)
    if not cur.fetchone():
        ct()
        print(bcolors.FAIL + "Incorrect password." + bcolors.RESET)
        log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user1_logs.txt", "a")
        log.write("" + currenttime + " - User3 was unsuccessfully logged into. Reason: incorrect password \n")
        log.close()
    else:
        ct()
        print(bcolors.OK + "Access granted.\n" + bcolors.RESET + "Redirecting you in 3 seconds...")
        log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user3_logs.txt", "a")
        log.write("" + currenttime + " - User3 was successfully logged into \n")
        log.close()
        t.sleep(3)
        subprocess.call(r"python C:\Users\Celt\dashenhanced\main\deps\dep1\users\user3.py 1", shell=True)
else:
    ct()
    print(bcolors.FAIL + "User not found. Make sure to ONLY use numbers while choosing your user!" + bcolors.RESET)
    log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
    log.write("" + currenttime + " - Someone was denied access to an user. Reason: no existing user matching input \n")
    log.close()