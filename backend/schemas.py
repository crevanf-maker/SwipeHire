from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import date


# ===============================
#       SKILL SCHEMAS (NEW)
# ===============================
class SkillBase(BaseModel):
    name: str


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ===============================
#       EDUCATION SCHEMAS (NEW)
# ===============================
class EducationBase(BaseModel):
    school: str
    degree: str
    field_of_study: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ===============================
#       EXPERIENCE SCHEMAS (NEW)
# ===============================
class ExperienceBase(BaseModel):
    title: str
    company: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None


class ExperienceCreate(ExperienceBase):
    pass


class Experience(ExperienceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ===============================
#       PROFILE SCHEMAS (UPDATED)
# ===============================
class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    headline: Optional[str] = None
    bio: Optional[str] = None
    resume_url: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int
    user_id: int
    # These lines create the nested JSON structure in API responses
    educations: List[Education] = []
    experiences: List[Experience] = []
    skills: List[Skill] = []
    model_config = ConfigDict(from_attributes=True)


# ===============================
#       USER & TOKEN SCHEMAS (Unchanged, but User now gets the richer Profile)
# ===============================
class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    profile: Optional[Profile] = None
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Optional[EmailStr] = None
