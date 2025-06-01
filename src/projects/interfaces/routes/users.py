from typing import List

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from projects.domain import UsersGateway
from projects.domain.entities import User
from projects.interfaces.schemas.users import UserSchema, UserSchemaResponse

users_router = APIRouter()


@users_router.post("/")
@inject
def create_user(
    user_create: UserSchema, gateway: FromDishka[UsersGateway]
) -> UserSchemaResponse:
    new_user: User = User(
        name=user_create.name,
        email=str(user_create.email),
        password=user_create.password,
    )
    added_user: User = gateway.add_user(new_user)
    return UserSchemaResponse(
        id=added_user.id,
        name=added_user.name,
        email=added_user.email,
        password=added_user.password,
        role=added_user.role,
    )


@users_router.get("/")
@inject
def get_users(gateway: FromDishka[UsersGateway]) -> List[User]:
    users: list[User] = gateway.get_users()
    return users


@users_router.get("/{user_id}")
@inject
def get_user(user_id: int, gateway: FromDishka[UsersGateway]) -> User:
    try:
        user: User = gateway.get_user(user_id)
        return user

    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")


@users_router.delete("/{user_id}")
@inject
def delete_user(user_id: int, gateway: FromDishka[UsersGateway]) -> bool:
    result: bool = gateway.remove_user(user_id)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to remove user")
    return result
