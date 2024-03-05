from typing import Optional, Any, List

from pydantic import BaseModel as _BaseModel
from pydantic.alias_generators import to_camel


class BaseModel(_BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
        str_strip_whitespace = True
        extra = "forbid"


class OutputMessage(BaseModel):
    success: bool
    message: Optional[str] = None
    detail: Optional[Any] = None
    data: Optional[Any] = None