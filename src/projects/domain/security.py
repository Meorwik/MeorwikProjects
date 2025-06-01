from datetime import datetime, timedelta
from typing import Optional, Any
from jose import JWTError, jwt
from jwt import InvalidTokenError
from passlib.context import CryptContext

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class JWTService:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        is_verified: bool = self.pwd_context.verify(plain_password, hashed_password)
        return is_verified

    def hash_password(self, password: str) -> str:
        result: str = self.pwd_context.hash(password)
        return result

    def create_access_token(self, data: dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        access_token: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return access_token

    def decode_token(self, token: str) -> dict[str, Any] | None:
        try:
            payload: dict[str, Any] = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload

        except JWTError:
            raise InvalidTokenError("Invalid token")