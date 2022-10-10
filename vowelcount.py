s=input("Enter the string : " )

vowel=0
for i in s:
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel=vowel+1

print("NUmber of vowels in the entered string is : ",vowel)