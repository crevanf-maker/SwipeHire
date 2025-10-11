from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Table, Date
from sqlalchemy.orm import relationship
from database import Base

# --- NEW: Association Table for Profile <-> Skill (Many-to-Many) ---
profile_skills_association = Table(
    "profile_skills",
    Base.metadata,
    Column(
        "profile_id",
        Integer,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("skill_id", Integer, ForeignKey("skills.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    profile = relationship(
        "Profile", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    headline = Column(String(100))
    bio = Column(Text)
    resume_url = Column(String(255), nullable=True)  # <-- NEW: For the resume path
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )

    user = relationship("User", back_populates="profile")
    # --- NEW: Relationships to Education, Experience, and Skills ---
    educations = relationship(
        "Education", back_populates="profile", cascade="all, delete-orphan"
    )
    experiences = relationship(
        "Experience", back_populates="profile", cascade="all, delete-orphan"
    )
    skills = relationship(
        "Skill", secondary=profile_skills_association, back_populates="profiles"
    )


# --- NEW: Education Model ---
class Education(Base):
    __tablename__ = "educations"
    id = Column(Integer, primary_key=True, index=True)
    school = Column(String(100), nullable=False)
    degree = Column(String(100), nullable=False)
    field_of_study = Column(String(100))
    start_date = Column(Date)
    end_date = Column(Date)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)

    profile = relationship("Profile", back_populates="educations")


# --- NEW: Experience Model ---
class Experience(Base):
    __tablename__ = "experiences"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)

    profile = relationship("Profile", back_populates="experiences")


# --- NEW: Skill Model ---
class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)

    profiles = relationship(
        "Profile", secondary=profile_skills_association, back_populates="skills"
    )
