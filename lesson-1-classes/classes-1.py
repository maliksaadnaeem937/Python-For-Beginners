
class Student:
    name:str
    def set_name(self,NAME):
        self.name=NAME
    def get_name(self):
        return self.name
        

student=Student()
student.set_name("saad")
name=student.get_name()
print(name)