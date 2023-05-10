from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import validator


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("username")
    def validate_username(cls, username):
        if not username or not len(username) > 3:
            raise ValueError("Username should be > 3 chars.")
        return username

    @validator("password")
    def validate_password(cls, password):
        if not password or not len(password) > 4:
            raise ValueError("Password must be > 4 chars")
        return password


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
