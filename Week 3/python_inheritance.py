#Inheritance

from typing import get_args


class info:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def name(self):
        print("Name : ", self.firstname, self.lastname)
    
    def age(self, age):
        print("Age : ", age)

    address = "22 NDC"

class Student(info):
    graduationyear = 2024
    def year(self):
        print("Graduation Year : ", self.graduationyear)
        

#multi-inher

class Grade(Student,info):
    graduationgrade = "Good"
    def grade(self):
        print("Graduation Grade : ", self.graduationgrade)

    date = "10/10"

s2 = Grade("A","B")
s2.name()
s2.age(20)
s2.year()
s2.grade()
print(s2.date)

