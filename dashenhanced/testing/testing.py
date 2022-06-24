from tabulate import tabulate
 
# assign data
mydata = [
    ["Nikhil", "Delhi"],
    ["Ravi", "Kanpur"],
    ["Manish", "Ahmedabad"],
    ["Prince", "Bangalore"]
]
 
# create header
head = ["Setting", "On/Off"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))