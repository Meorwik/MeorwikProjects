from dishka import inject
from fastapi import APIRouter, Depends, HTTPException
from utils.auth import create_access_token, hash_password

from projects.domain.protocols.users_protocol import UsersGateway
from projects.interfaces.schemas import UserSchema, UserSchemaResponse
from projects.interfaces.schemas.user import UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
def register_user(
    user_data: UserSchema, gateway: UsersGateway = Depends()
) -> UserSchemaResponse:
    existing_user = gateway.get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user_data.password)
    new_user = gateway.create_user(email=user_data.email, hashed_password=hashed)

    return UserSchemaResponse(id=new_user.id, email=new_user.email)
