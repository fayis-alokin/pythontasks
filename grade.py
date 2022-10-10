marks=[]

subjects=[
"Mathematics",
"Physics",
"Chemistry",
"computer Science",
"Statistics",
"electronics"]

total_mark=0

for i in range(6):
    print("Enter the mark of "+subjects[i])
    mark=int(input())
    marks.append(mark)
    total_mark=total_mark+mark


avg=(total_mark)/6
print("Your Average  mark is :",round(avg,2))

if avg>95 :
    print("Grade is A+")
elif avg>=90 and avg<=95 :
    print("Grade is A")
elif avg>=80 and avg<90 :
    print("Grade is B+")
elif avg>=70 and avg<80 :
    print("Grade is B")
elif avg>=60 and avg<70 :
    print("Grade is C+")
elif avg>=50 and avg<60 :
    print("Grade is C")
elif avg>=40 and avg<50 :
    print("Grade is D+")
else :
    print("Failed")

