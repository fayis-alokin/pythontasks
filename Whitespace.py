import re

text=input("Enter a string: ")
d={' ':'_','_':' '}
print("Text before conversion : ",text)
print("Text after conversion : ")
print(re.sub(r'[ ]',lambda m:d[m[0]],text))