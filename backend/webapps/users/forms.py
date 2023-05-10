from typing import Optional

from fastapi import Request
from pydantic import ValidationError
from schemas.users import UserCreate


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: list = []
        self.username: Optional[str] = ""
        self.email: Optional[str] = ""
        self.password: Optional[str] = ""

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.email = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        try:
            UserCreate.validate(
                {
                    "username": self.username,
                    "email": self.email,
                    "password": self.password,
                }
            )
        except ValidationError as e:
            self.errors.extend([error["msg"] for error in e.errors()])
        if not self.errors:
            return True
        return False
