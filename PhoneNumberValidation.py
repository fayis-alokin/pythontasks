import re

num=input("Enter the number : ")

x=re.match("^\\+?[1-9][0-9]{10,10}$",num)

if x.match(num):
    print("valid")

else:
    print("Invalid")

