from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=16, le=60)
    email: str = Field(...)
    cgpa: float = Field(..., ge=0.0, le=4.0)
    phone: str = Field(default="Not Provided")
    is_active: bool = Field(default=True)
    skills: list[str] = Field(default_factory=list, min_length=1)
    city: str = Field(default="Islamabad")
    semester: int = Field(default=1, ge=1, le=8)
    scholarship: bool = Field(default=False)
