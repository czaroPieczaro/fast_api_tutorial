import time
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Languages(str, Enum):
    PY = "Python"
    JAVA = "JAVA"
    GO = "GO"


class Comment(BaseModel):
    text: Optional[str] = None


class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool
    language: Languages = Languages.PY
    created_at: datetime = Field(default_factory=datetime.now)
    comments: Optional[list[Comment]]


print(
    Blog(
        title="1st blog",
        language="JAVA",
        is_active=True,
        comments=[{"text": "1st"}, {"text": "2nd"}],
    )
)
time.sleep(5)
print(Blog(title="1st blog", language="JAVA", is_active=True))
# print(Blog(title="1st blog", language="C++", is_active=True))

# Blog(title='Second One',is_active='yup!')
