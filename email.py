import re

mail=input("Enter your mail here : ")

firstpart=re.split("@",mail)

print(firstpart[0])

print(firstpart[0]+"@")