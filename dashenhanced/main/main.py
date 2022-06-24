import os
from os import write
import getpass as gp
from datetime import datetime
import subprocess
import time as t
import sqlite3 as sql

# variables

now = datetime.now()
currenttime = str(now)
con = sql.connect("data.db")
cur = con.cursor()

#functions

def enter():
    print("")

def ct():
    os.system('cls')

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

#code

ct()

print(bcolors.WARNING + "NOTE: This project is still in alpha stage and is nowhere near finished. Further information about the future of this project can be found on the project's GitHub page." + bcolors.RESET)
print("\nSELECT YOUR DEPARTMENT")
enter()
print("Insert the number of your department displayed below.")
enter()
print("1: Department A")
print("2: Department B")
print("3: Department C")
enter()

depselect = input("Department no.: ")

if depselect == "1":
    ct()
    print("Selected department: Dep1")
    deppass = gp.getpass("Department password:")
    statement = f"SELECT username from dep1 WHERE password='{deppass}';"
    cur.execute(statement)
    if not cur.fetchone():
        ct()
        print(bcolors.FAIL + "Access denied." + bcolors.RESET)
        log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
        log.write("" + currenttime + " - Dep1 was unsuccessfully accessed. Reason: incorrect password \n")
        log.close()
    else:
        ct()
        print(bcolors.OK + "Access granted." + bcolors.RESET)
        print("Redirecting you in 3 seconds...")
        log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
        log.write("" + currenttime + " - Dep1 was successfully accessed \n")
        log.close()
        t.sleep(3)
        ct()
        subprocess.call(r"python C:\Users\Celt\dashenhanced\main\deps\dep1\dep1.py 1", shell=True)


elif depselect == "2":
    ct()
    print("Selected department: Dep2")
    deppass = gp.getpass("Department password:")
    statement = f"SELECT username from dep2 WHERE password='{deppass}';"
    cur.execute(statement)
    if not cur.fetchone():
        ct()
        print(bcolors.FAIL + "Access denied." + bcolors.RESET)
        log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
        log.write("" + currenttime + " - Dep2 was unsuccessfully accessed. Reason: incorrect password \n")
        log.close()
    else:
        ct()
        print(bcolors.OK + "Access granted." + bcolors.RESET)
        print("Redirecting you in 3 seconds...")
        log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
        log.write("" + currenttime + " - Dep2 was successfully accessed \n")
        log.close()
        t.sleep(3)
        ct()
        subprocess.call(r"python C:\Users\Celt\dashenhanced\main\deps\dep2\dep2.py 1", shell=True)

elif depselect == "3":
    ct()
    print("Selected department: Dep3")
    deppass = gp.getpass("Department password:")
    statement = f"SELECT username from dep3 WHERE password='{deppass}';"
    cur.execute(statement)
    if not cur.fetchone():
        ct()
        print(bcolors.FAIL + "Access denied." + bcolors.RESET)
        log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
        log.write("" + currenttime + " - Dep3 was unsuccessfully accessed. Reason: incorrect password \n")
        log.close()
    else:
        ct()
        print(bcolors.OK + "Access granted." + bcolors.RESET)
        print("Redirecting you in 3 seconds...")
        log = open(r"C:\Users\Celt\dashenhanced\logging\departmentlogs.txt", "a")
        log.write("" + currenttime + " - Dep3 was successfully accessed \n")
        log.close()
        t.sleep(3)
        ct()
        subprocess.call(r"python C:\Users\Celt\dashenhanced\main\deps\dep3\dep3.py 1", shell=True)