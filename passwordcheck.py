username=input("Set your username : ")
pas=input("Set your password : ")
conf_pas=input("Confirm your password : ")

if conf_pas != pas :
    print("Passwords are not matching, Please try again... :")


entered_username=input("Enter your username : ")
entered_pas=input("Enter your password : ")

if entered_username!=username or entered_pas!=conf_pas :
    print("Username or password entered incorrectly,Please try again...")
else :
    print("Welcome ",username)
