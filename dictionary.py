
l1=[]
l2=[]

s=int(input("Enter the size "))

print("Enter the value s for first list : ")
for i in range(s):
    a=input("values : ")
    l1.append(int(a))

print("Enter the values for second list : ")
for i in range(s):
    b=input("values : ")
    l2.append((b))

dict={}

for i in range(s):
    dict[l1[i]]=l2[i]

print("The final result is : ",dict)

