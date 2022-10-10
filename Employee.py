E_id=int(input("Enter the employee id : "))
E_name=input("Enter your name : ")
E_BP=int(input("Enter your basic pay : "))

print("Dear, ",E_name)

if E_BP>10000 :
    HRA=(15/100)*E_BP
    print("Your H.R.A is : ",HRA)
    DA=(8/100)*E_BP
    print("Your DA is : ",DA)
    Net=HRA+DA+E_BP
    print("Your net salary is : ",Net)
elif E_BP>=5000 and E_BP<=10000 :
    HRA=(10/100)*E_BP
    print("Your HRA is : ",HRA)
    DA=(5/100)*E_BP
    print("Your DA is : ",DA)
    Net=HRA+DA+E_BP
    print("Your net salary is : ",Net)
else :
    HRA=(5/100)*E_BP
    print("Your HRA is : ",HRA)
    DA=(3/100)*E_BP
    print("Your DA is : ",DA)
    Net=HRA+DA+E_BP
    print("Your net salary is : ",Net)
    

