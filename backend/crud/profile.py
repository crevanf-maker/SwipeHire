from sqlalchemy.orm import Session
import models
import schemas


def get_profile_by_user_id(db: Session, user_id: int):
    return db.query(models.Profile).filter(models.Profile.user_id == user_id).first()


def create_user_profile(db: Session, profile: schemas.ProfileCreate, user_id: int):
    db_profile = models.Profile(**profile.model_dump(), user_id=user_id)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


# --- ADD THESE NEW FUNCTIONS ---


def add_education_to_profile(
    db: Session, education: schemas.EducationCreate, profile_id: int
):
    """
    Adds a new education entry to a user's profile.
    """
    db_education = models.Education(**education.model_dump(), profile_id=profile_id)
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education


def add_experience_to_profile(
    db: Session, experience: schemas.ExperienceCreate, profile_id: int
):
    """
    Adds a new work experience entry to a user's profile.
    """
    db_experience = models.Experience(**experience.model_dump(), profile_id=profile_id)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience


def add_skill_to_profile(db: Session, profile: models.Profile, skill: models.Skill):
    """
    Links an existing skill to a user's profile.
    """
    profile.skills.append(skill)
    db.commit()
    db.refresh(profile)
    return profile
