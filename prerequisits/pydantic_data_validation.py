from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator


class Blog(BaseModel):
    title: str = Field(..., min_length=5)
    is_active: bool
    password: str
    confirm_password: str

    @validator("title")
    def validate_no_sql_injection(cls, value):
        if "delete from" in value:
            raise ValueError("Our terms strictly prohobit SQLInjection Attacks")
        return value

    @root_validator()
    def verify_passwords_match(cls, values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("Passwords don't match!")

        return values


# print(Blog(title="1stssa delete from", is_active=True))
print(Blog(title="1stssa", is_active=True, password="123", confirm_password="1213"))
