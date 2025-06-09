class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def dispaly(self):
        print(f"Name: {self.name} Marks: {self.marks}")

s1 = Student("Ather", 100)

s1.dispaly()


    