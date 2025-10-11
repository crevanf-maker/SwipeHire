from sqlalchemy.orm import Session
import models
import schemas


def get_skill_by_name(db: Session, name: str):
    """
    Fetches a single skill by its name (case-insensitive).
    """
    return db.query(models.Skill).filter(models.Skill.name.ilike(name)).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100):
    """
    Fetches a list of all skills.
    """
    return db.query(models.Skill).offset(skip).limit(limit).all()


def create_skill(db: Session, skill: schemas.SkillCreate):
    """
    Creates a new skill in the database.
    """
    db_skill = models.Skill(name=skill.name.title())  # Standardize to Title Case
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_or_create_skill(db: Session, skill: schemas.SkillCreate):
    """
    Checks if a skill exists. If so, returns it. If not, creates it.
    """
    db_skill = get_skill_by_name(db, name=skill.name)
    if db_skill:
        return db_skill
    return create_skill(db=db, skill=skill)
