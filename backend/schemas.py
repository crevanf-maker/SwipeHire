from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# ===============================
#       USER SCHEMAS
# ===============================


class UserBase(BaseModel):
    """Shared properties for a user."""

    email: EmailStr
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    """Properties to receive when creating a new user."""

    password: str


class UserUpdate(BaseModel):
    """Properties to receive when updating a user."""

    password: Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    """Properties to return to the client."""

    id: int
    model_config = ConfigDict(from_attributes=True)


# ===============================
#       TOKEN SCHEMAS
# ===============================


class Token(BaseModel):
    """Properties for the token response after login."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Properties to store in the JWT payload."""

    email: Optional[EmailStr] = None
