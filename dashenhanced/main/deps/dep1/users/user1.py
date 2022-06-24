import os
import msvcrt as m
import sqlite3 as sql
from datetime import datetime
import time as t
import random
from tabulate import tabulate

file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
read = file.read()
quotes = ("'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.'", "'First, solve the problem. Then, write the code.'", "'Experience is the name everyone gives to their mistakes.'", "'In order to be irreplaceable, one must always be different", "Java is to JavaScript what car is to Carpet.'", "'Knowledge is power.'", "'Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code.'", "'Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.'", "'Code is like humor. When you have to explain it, it's bad.'", "'Fix the cause, not the symptom.'", "'Optimism is an occupational hazard of programming: feedback is the treatment.'", "'Simplicity is the soul of efficiency.'", "'Before software can be reusable it first has to be usable.'")

if "1=off" in read:
    dtime = ""
elif "1=on" in read:
    dnow = datetime.now()
    time = str(dnow)
    dtime = "| " + time
now = datetime.now()
currenttime = str(now)
con = sql.connect("data.db")
cur = con.cursor()
personalname = "John Doe"
logged_in = True

def wait():
    m.getch()

def ct():
    os.system('cls')

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

while logged_in == True:
    ct()
    file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
    read = file.read()
    if "2=off" in read:
        print("NOTE: You may be currently using an outdated version. Check the GitHub page for new versions (use 'github' in the HOME menu).")
    elif "2=on" in read:
        print(bcolors.WARNING + "NOTE: You may be currently using an outdated version. Check the GitHub page for new versions (use 'github' in the HOME menu)." + bcolors.RESET)
    print("\n[logged in] | > HOME < | Apps | Settings | Changelogs " + dtime + "\n")
    print("Welcome back, " + personalname + ".\n")
    print("A new update has been released. Type 'devlogs' to check it out.")
    #sqlite, check if new rows have been created in mail category
    print("You can check your messages by using 'inbox' in the APPS tab.\n")
    #
    file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
    read = file.read()
    if "3=on" in read:
        quote = random.choice(quotes)
        rquote = bcolors.OK + quote + "\n" + bcolors.RESET
        print(rquote)
    print("Type 'help' for a list of commands.")

    command = input("> ")

    if command == "devlogs":
        ct()
        print("[logged in] | Home | Apps | Settings | > CHANGELOGS < " + dtime + "\n")
        print("ALPHA RELEASE\n\nWelcome to the Matrix. Just kidding, welcome to the alpha stage. Nothing near finished nor polished, just bugtesting and releasing new stuff - you (probably) know the drill ;)")
        print("SQLite has been implemented and fully works. There may be some bugs here and there, but it overall should be working perfectly fine.\n\nIf you do encounter bugs, let us know on our GitHub page ('github' as command).")
        print("\nPress any key to go back to the HOME menu.")
        wait()
    elif command == "apps":
        appcmd = None
        while appcmd != "back":
            ct()
            print("[logged in] | Home | > APPS < | Settings | Changelogs " + dtime + "\n")
            print("APPS\n")
            print("inbox | this is where your messages go")
            print("  msg | send a message to someone")
            print("\nType in which app you wish to use below. Type 'back' to go back to the HOME menu.")
            appcmd = input("> ")
            if appcmd == "inbox":
                log = open(r"C:\Users\Celt\dashenhanced\logging\userlogs\dep1\user1_logs.txt", "a")
                log.write("" + currenttime + " - User1's message inbox was accessed \n")
                log.close()
                ct()
                print("[logged in] | Home | > APPS < | Settings | Changelogs\n")
                print("MESSAGE INBOX \n")
                cur.execute("SELECT rowid, * FROM dep1_user1_messages ORDER BY rowid")
                messages = cur.fetchall()
                for item in messages:
                    if item == None:
                        file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
                        read = file.read()
                        if "2=off" in read:
                            print("No new messages.")
                        elif "2=on" in read:
                            print(bcolors.OK + "No new messages." + bcolors.RESET)
                    else:
                        print(item)
                file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
                read = file.read()
                if "2=off" in read:
                    print("\nPress any key to go back to the APPS tab. NOTE: All messages displayed here will be removed from your inbox.")
                elif "2=on" in read:
                    print("\nPress any key to go back to the APPS tab." + bcolors.WARNING + " NOTE: All messages displayed here will be removed from your inbox." + bcolors.RESET)
                wait()
                cur.execute("DELETE FROM dep1_user1_messages;")
                con.commit() 
            elif appcmd == "msg":
                usermsg = None
                while usermsg != "back":
                    ct()
                    print("[logged in] | Home | > APPS < | Settings | Changelogs " + dtime + "\n")
                    print("SEND MESSAGE \n")
                    file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
                    read = file.read()
                    if "2=off" in read:
                        print("Select user to message. NOTE: You can only message users from your department.\n")
                    elif "2=on" in read: 
                        print("Select user to message. Type 'back' to return to the APPS tab. " + bcolors.WARNING + "NOTE: You can only message users from your department.\n" + bcolors.RESET)
                    print("1 = User2\n2 = User3\n")
                    usermsg = input("> ")
                    if usermsg == "1":
                        ct()
                        print("[logged in] | Home | > APPS < | Settings | Changelogs " + dtime + "\n")
                        print("SEND MESSAGE \n")
                        print("What do you want to send to User2?\n")
                        msg = input("> ")
                        cur.execute("INSERT INTO dep1_user2_messages VALUES ('" + msg + "')")
                        con.commit()
                        ct()
                        print("Message sent.\n\nPress any key to go back to the MESSAGE app.")
                        wait()
                    elif usermsg == "2":
                        ct()
                        print("[logged in] | Home | > APPS < | Settings | Changelogs " + dtime + "\n")
                        print("SEND MESSAGE \n")
                        print("What do you want to send to User3?\n")
                        msg = input("> ")
                        cur.execute("INSERT INTO dep1_user3_messages VALUES ('" + msg + "')")
                        con.commit()
                        ct()
                        print("Message sent.\n\nPress any key to go back to the MESSAGE app.")
                        wait()
                    elif usermsg == "back":
                        pass
                    else:
                        ct()
                        file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
                        read = file.read()
                        if "2=off" in read:
                            print("Failed to find existing user matching given input. Make sure to ONLY use numbers!")
                        elif "2=on" in read:
                            print(bcolors.FAIL + "Failed to find existing user matching given input. Make sure to ONLY use numbers!" + bcolors.RESET)
                        print("\nPress any key to return to the MESSAGE app.")
                        wait()
                        pass
            elif appcmd == "back":
                pass
    elif command == "settings":
        setting = None
        while setting != "back":
            ct()
            file = open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", "r")
            read = file.read()
            
            if "1=off" in read:
                setting1 = "Off"
            elif "1=on" in read:
                setting1 = "On"
            if "2=off" in read:
                setting2 = "Off"
            elif "2=on" in read:
                setting2 = "On"
            if "3=off" in read:
                setting3 = "Off"
            elif "3=on" in read:
                setting3 = "On" 

            print("[logged in] | Home | Apps | > SETTINGS < | Changelogs " + dtime + "\n\nSETTINGS")
            
            settingdata = [
                ["Display current time (requires restart)", setting1],
                ["Colored error/warning output", setting2],
                ["Quotes on homepage", setting3]
            ]

            print(tabulate(settingdata, tablefmt="presto"))

            print("\nType the number of the setting you want to turn on/off below. (type 'back' to go back to the HOME menu)")
            setting = input("> ")
            if setting == "1":
                if setting1 == "On":
                    filedata = read.replace('1=on', '1=off')
                    with open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", 'w') as file:
                        file.write(filedata)
                elif setting1 == "Off":
                    filedata = read.replace('1=off', '1=on')
                    with open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", 'w') as file:
                        file.write(filedata)
            elif setting == "2":
                if setting2 == "On":
                    filedata = read.replace('2=on', '2=off')
                    with open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", 'w') as file:
                        file.write(filedata)
                elif setting2 == "Off":
                    filedata = read.replace('2=off', '2=on')
                    with open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", 'w') as file:
                        file.write(filedata)
            elif setting == "3":
                if setting3 == "On":
                    filedata = read.replace('3=on', '3=off')
                    with open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", 'w') as file:
                        file.write(filedata)
                elif setting3 == "Off":
                    filedata = read.replace('3=off', '3=on')
                    with open(r"C:\Users\Celt\dashenhanced\main\deps\dep1\users\user1_settings.txt", 'w') as file:
                        file.write(filedata)
            elif setting == "back":
                pass
    elif command == "github":
        ct()
        print("https://github.com/actualthecelt/dashenhanced")
        print("Press any key to go back to the HOME menu.")
        wait()
    elif command == "help":
        ct()
        print("[logged in] | > HOME < | Apps | Settings | Changelogs " + dtime + "\n")
        print("LIST OF COMMANDS")
        print("    apps | opens the APPS tab\nsettings | opens your SETTINGS\n devlogs | opens the CHANGELOG\n github | shows the dashboard's GITHUB link\n\nPress any key to go back to the HOME menu.")
        wait()