from pydantic import BaseModel, EmailStr

from projects.interfaces.schemas.enums.roles import Roles


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Roles = Roles.user

class UserSchemaResponse(UserSchema):
    id: int
    email: str