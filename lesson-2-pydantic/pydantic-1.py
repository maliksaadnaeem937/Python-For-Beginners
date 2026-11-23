
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

student = Student(name="Saad", age=22)

print(student)
