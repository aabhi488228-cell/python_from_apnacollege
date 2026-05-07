class Student:
    college_name = "abc college"
    name = "anonymous" 

    def __init__(self,fullname,marks): ##constructor 
        self.name = fullname
        self.marks = marks
        print("adding new student in the database..")

s1 = Student("karan",97.7)
print(s1.name)
print(s1.marks)         