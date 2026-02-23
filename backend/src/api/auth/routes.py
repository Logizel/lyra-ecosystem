from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

from api.auth.authentication import create_jwt_token
from services.database.postgres_client import PostgresClient

router = APIRouter(prefix="/auth", tags=["authentication"])

client = PostgresClient()


class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserRegister):
    """Register new user and return JWT token."""
    try:
        user = client.create_user(
            email=user_data.email, plain_password=user_data.password
        )

        token = create_jwt_token(str(user.id))
        return TokenResponse(access_token=token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Registration failed: {str(e)}",
        )


@router.post("/login", response_model=TokenResponse)
def login(credentials: UserLogin):
    """Login user and return JWT token."""
    user = client.authenticate_user(
        email=credentials.email, plain_password=credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    token = create_jwt_token(str(user.id))
    return TokenResponse(access_token=token)
