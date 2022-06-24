import os
from tabulate import tabulate
 
# assign data
settingdata = [
    ["Display current time (requires restart)", "Delhi"],
    ["Colored error/warning output", "Kanpur"],
    ["Quotes on homepage", "Ahmedabad"]
]

head = ["Setting", "On/Off"]

print(tabulate(settingdata, headers=head, tablefmt="grid"))

print("Customize dashboard\n ↳ 1: Display current time | ""  (requires restart)\n ↳ 2: Colored error/warning output | ")
print(" ↳ 3: Quotes on homepage | ")