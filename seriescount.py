l1=["lock","key","gate","lock","lock","gate","key","door","lock","gate","mate","gate","key","mat","lock"]


dict={}
count=0

for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]==l1[j]:
            count=count+1
    if count>=3:
        dict[l1[i]]=count
    count=0


print(dict)
