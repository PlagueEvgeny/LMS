# schemas/user.py  
from pydantic import BaseModel
from pydantic import constr
from pydantic import Field
from datetime import datetime

class CourseCreate(BaseModel):  
    name: str = Field(min_length=3, max_length=50, examples="Python для начинающих")
    slug: constr(regex=r"^[a-z0-9_-]+$")
    desc: str = Field(examples="Краткое описание курса")
    about_course: str = Field(examples="Продробная программа курса")
    image: str | None = None
    is_active: bool = True
    teacher_id: int


class CourseResponse(BaseModel):  
    id = int
    name: str
    slug: str
    desc: str
    about_course: str
    image: str  
    is_active: bool  
    teacher_id: int
    created_at: datetime  
    updated_at: datetime | None  

    class Config:  
        orm_mode = True  # нужно для работы с ORM (как в Django моделях) 