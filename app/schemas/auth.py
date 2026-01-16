from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access: str
    refresh: str
