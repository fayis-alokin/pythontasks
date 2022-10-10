even_sum=0
odd_sum=0
for i in range(15,36):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i

print("sum of even numbers from 15-35 is : ",even_sum)
print("sum of odd numbers from 15-35 is : ",odd_sum)


