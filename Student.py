class Student:
    def __init__(self):
        self.rollno=0
        self.name=""

    def get_data(self):
        self.rollno=input("Enter your roll number : ")
        self.name=input("Enter your name : ")

    def print_data(self):
        print("Name is : ",self.name)
        print("Roll Number is : ",self.rollno)

class marks(Student):
    def __init__(self):
        self.physics=0
        self.chemistry=0
        self.biology=0
        self.mathematics=0
        self.english=0
        self.computer=0

    def input_data(self):
        self.get_data()
        self.physics=int(input("Enter the mark of Physics : "))
        self.chemistry=int(input("Enter the mark of Chemistry : "))
        self.biology=int(input("Enter the mark of Biology : "))
        self.mathematics=int(input("Enter the mark of Mathematics : "))
        self.english=int(input("Enter the mark of English : "))
        self.computer=int(input("Enter the mark of Computer : "))

    def out_data(self):
        self.print_data()
        print("Mark of Physics is : ",self.physics)
        print("Mark of Chemistry is : ",self.chemistry)
        print("Mark of Biology is : ",self.biology)
        print("Mark of Mathematics is : ",self.mathematics)
        print("Mark of English is : ",self.english)
        print("Mark of Computer is : ",self.computer)

Student1=marks()
Student1.input_data()
Student1.out_data()


        

        