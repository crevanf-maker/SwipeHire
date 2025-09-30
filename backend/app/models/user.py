from sqlalchemy import Column, String, Boolean, DateTime, Enum as SQLEnum, Text, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
import enum
from app.models.base import BaseModel, SoftDeleteMixin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AccountType(str, enum.Enum):
    JOB_SEEKER = "job_seeker"
    EMPLOYER = "employer"
    ADMIN = "admin"


class OAuthProvider(str, enum.Enum):
    GOOGLE = "google"
    LINKEDIN = "linkedin"
    GITHUB = "github"
    FACEBOOK = "facebook"
    LOCAL = "local"


class User(BaseModel, SoftDeleteMixin):
    __tablename__ = "users"
    
    # Basic Info
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=True)
    
    # Verification
    is_email_verified = Column(Boolean, default=False)
    is_phone_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True, index=True)
    
    # Account Info
    last_login_at = Column(DateTime(timezone=True), nullable=True)
    account_type = Column(SQLEnum(AccountType), default=AccountType.JOB_SEEKER, nullable=False, index=True)
    
    # OAuth
    oauth_provider = Column(SQLEnum(OAuthProvider), default=OAuthProvider.LOCAL)
    oauth_id = Column(String(255), nullable=True, index=True)
    
    # Profile
    profile_picture_url = Column(Text, nullable=True)
    
    # Relationships
    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    preferences = relationship("UserPreferences", back_populates="user", uselist=False, cascade="all, delete-orphan")
    sessions = relationship("UserSession", back_populates="user", cascade="all, delete-orphan")
    skills = relationship("Skill", back_populates="user", cascade="all, delete-orphan")
    experiences = relationship("Experience", back_populates="user", cascade="all, delete-orphan")
    education = relationship("Education", back_populates="user", cascade="all, delete-orphan")
    certifications = relationship("Certification", back_populates="user", cascade="all, delete-orphan")
    languages = relationship("Language", back_populates="user", cascade="all, delete-orphan")
    swipes = relationship("Swipe", back_populates="user", cascade="all, delete-orphan")
    applications = relationship("Application", back_populates="user", cascade="all, delete-orphan")
    saved_jobs = relationship("SavedJob", back_populates="user", cascade="all, delete-orphan")
    resumes = relationship("Resume", back_populates="user", cascade="all, delete-orphan")
    cover_letters = relationship("CoverLetter", back_populates="user", cascade="all, delete-orphan")
    recommendations = relationship("AIRecommendation", back_populates="user", cascade="all, delete-orphan")
    match_scores = relationship("MatchScore", back_populates="user", cascade="all, delete-orphan")
    
    def set_password(self, password: str) -> None:
        """Hash and set password"""
        self.password_hash = pwd_context.hash(password)
    
    def verify_password(self, password: str) -> bool:
        """Verify password against hash"""
        return pwd_context.verify(password, self.password_hash)
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
