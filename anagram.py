
import random

empty=[]

str=input("Enter a string: ")
lst=list(str)

while True:
    random.shuffle(lst)
    x=''.join(lst)
    if x not in empty:
        empty.append(x)
    else:
        break
print(empty)

