class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod ##decorator
    def hello():
        print("hello abhi")

    def get_avg(self):
            sum = 0
            for val in self.marks:
                sum += val
            print("hi",self.name,"your avg marks is :",sum/3)

s1 = student("tonny stark",[99,98,97])
s1.get_avg()