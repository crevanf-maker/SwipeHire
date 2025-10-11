from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

import schemas
import crud.skill as crud
from database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Skill)
def create_new_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):

    # Create a new skill in the system.

    return crud.create_skill(db=db, skill=skill)


@router.get("/", response_model=List[schemas.Skill])
def read_all_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all skills.
    """
    skills = crud.get_skills(db, skip=skip, limit=limit)
    return skills
