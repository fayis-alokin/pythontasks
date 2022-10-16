from ast import pattern
import re


num=input("Enter the number : ")

pattern=re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")

if pattern.match(num):
    print("valid number : ")

else:
    print("Invalid number : ")

