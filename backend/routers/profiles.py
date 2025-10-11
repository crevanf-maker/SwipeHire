# /backend/routers/profiles.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import security

import crud.profile as profile_crud
import crud.skill as skill_crud

from database import get_db

router = APIRouter()

# --- Base Profile Routes (Existing) ---


@router.post("/", response_model=schemas.Profile)
def create_profile_for_current_user(
    profile: schemas.ProfileCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(security.get_current_user),
):
    if current_user.profile:
        raise HTTPException(status_code=400, detail="User already has a profile")
    return profile_crud.create_user_profile(
        db=db, profile=profile, user_id=current_user.id
    )


@router.get("/me/", response_model=schemas.Profile)
def read_current_user_profile(
    current_user: models.User = Depends(security.get_current_user),
):
    if not current_user.profile:
        raise HTTPException(
            status_code=404, detail="Profile not found for current user"
        )
    return current_user.profile


# --- NEW Endpoints for Profile Details ---


@router.post("/me/education/", response_model=schemas.Education)
def add_education_to_my_profile(
    education: schemas.EducationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(security.get_current_user),
):
    if not current_user.profile:
        raise HTTPException(
            status_code=404, detail="Profile not found, create one first."
        )
    return profile_crud.add_education_to_profile(
        db=db, education=education, profile_id=current_user.profile.id
    )


@router.post("/me/experience/", response_model=schemas.Experience)
def add_experience_to_my_profile(
    experience: schemas.ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(security.get_current_user),
):
    if not current_user.profile:
        raise HTTPException(
            status_code=404, detail="Profile not found, create one first."
        )
    return profile_crud.add_experience_to_profile(
        db=db, experience=experience, profile_id=current_user.profile.id
    )


@router.post("/me/skills/", response_model=schemas.Profile)
def add_skill_to_my_profile(
    skill: schemas.SkillCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(security.get_current_user),
):
    if not current_user.profile:
        raise HTTPException(
            status_code=404, detail="Profile not found, create one first."
        )

    # Check if skill exists, or create it if it doesn't
    db_skill = skill_crud.get_or_create_skill(db, skill=skill)

    # Check if skill is already linked to profile
    if db_skill in current_user.profile.skills:
        raise HTTPException(status_code=400, detail="Skill already added to profile.")

    # Link the skill to the profile
    return profile_crud.add_skill_to_profile(
        db=db, profile=current_user.profile, skill=db_skill
    )
