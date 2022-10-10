list1=[44,64,69,37,76,83,95,97]

dict1={'soj0':44,'thomas':69,'tom':76,'jack':11}

for i in list1[:]:
    if i not in dict1.values():
        list1.remove(i)

print(list1)