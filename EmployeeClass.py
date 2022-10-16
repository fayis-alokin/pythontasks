class Employee:
    def __init__(self) :
        self.e_id=0
        self.e_name=""
        self.e_designation=""
        self.e_address=""
        self.e_phone=0
    def get_data(self):
        self.e_id=int(input("Enter you ID : "))
        self.e_name=input("Enter your name : ")
        self.e_designation=input("Enter your designation : ")
        self.e_address=input("Enter your address : ")
        self.e_phone=int(input("Enter your mobile number : "))

    def print_data(self):
        self.get_data()
        print("Your ID is : ",self.e_id)
        print("Your name is : ",self.e_name)
        print("Your designation is : ",self.e_designation)
        print("Your address is : ",self.e_address)
        print("Your mobile number is : ",self.e_phone)

class salary(Employee):
    def __init__(self):
        self.DA=0
        self.HRA=0
        self.PF=0
        self.basicpay=0
        self.netpay=0

    def get_basicpay(self):
        self.basicpay=int(input("Enter your basic pay : "))

    def calculate(self):
        if(self.basicpay>10000):
            self.DA=(8/100)*self.basicpay
            self.HRA=(12/100)*self.basicpay
            self.PF=(10/100)*self.basicpay

            self.netpay=self.DA+self.HRA+self.PF

            

        elif(self.basicpay<=10000 and self.basicpay>5000):
            self.DA=(5/100)*self.basicpay
            self.HRA=(8/100)*self.basicpay
            self.PF=(5/100)*self.basicpay

            self.netpay=self.DA+self.HRA+self.PF


        else:
            self.DA=(3/100)*self.basicpay
            self.HRA=(5/100)*self.basicpay
            self.PF=(1/100)*self.basicpay

            self.netpay=self.DA+self.HRA+self.PF

    def display(self):
        self.print_data()

        print("Your basic pay is : ",self.basicpay)
        print("Your DA is : ",self.DA)
        print("Your HRA is : ",self.HRA)
        print("Your PF is : ",self.PF)
        print("Your net pay is ",self.netpay)

e1=salary()
e1.get_basicpay()
e1.calculate()

e1.display()



        




