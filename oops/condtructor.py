class Student:
##parameterized constructors

    def __init__(self,fullname,marks): ##constructor 
        self.name = fullname
        self.marks = marks
        print("adding new student in the database..")

s1 = Student("karan",97.7)
print(s1.name)
print(s1.marks)

s2 = Student("taufiq",98.9)
print(s2.name)
print(s2.marks)

##default constructor
class Student:

    def __init__(self): ##constructor 
        pass