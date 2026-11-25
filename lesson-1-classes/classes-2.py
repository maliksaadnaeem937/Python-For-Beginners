class Student:
    name: str
    age: int

    def __init__(self, NAME, AGE):
        self.name = NAME
        self.age = AGE

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_name_and_age(self):
        return self.name, self.age


student=Student(NAME="saad",AGE=20)
name,age=student.get_name_and_age()
print("Name=",name)
print("Age=",age)