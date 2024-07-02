class Student:
    def __init__(self, name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def set_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max):
        self.name=name
        self.max=max
        self.students=[]

    def add_student(self,name):
        if len(self.students)<self.max:
            self.students.append(name)
            return True
        return False

    def avg(self):
        total=0
        for student in self.students:
            total+=student.set_grade()
        return total/len(self.students)

s1=Student("Tim", 23, 98)
s2=Student("Jom", 26, 68)
s3=Student("MAc", 45, 56)

c1=Course("Science",2)
print(c1.add_student(s1))
print(c1.add_student(s2))
print(c1.add_student(s3))
print(c1.avg())