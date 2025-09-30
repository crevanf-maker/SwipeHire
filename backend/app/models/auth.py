from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text, Enum as SQLEnum, JSON
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel


class UserSession(BaseModel):
    __tablename__ = "user_sessions"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    token = Column(String(500), unique=True, nullable=False, index=True)
    refresh_token = Column(String(500), nullable=True)
    
    # Device Info
    device_info = Column(JSON, nullable=True)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    
    # Status
    is_active = Column(Boolean, default=True, index=True)
    expires_at = Column(DateTime(timezone=True), nullable=False, index=True)
    last_activity_at = Column(DateTime(timezone=True), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="sessions")


class SalaryPeriod(str, enum.Enum):
    HOURLY = "hourly"
    MONTHLY = "monthly"
    YEARLY = "yearly"


class UserPreferences(BaseModel):
    __tablename__ = "user_preferences"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    
    # Job Preferences
    preferred_job_titles = Column(JSON, default=list)
    preferred_locations = Column(JSON, default=list)
    preferred_industries = Column(JSON, default=list)
    job_types = Column(JSON, default=["full_time"])  # full_time, part_time, contract, etc.
    work_mode = Column(JSON, default=["remote", "hybrid", "onsite"])
    
    # Salary
    min_salary = Column(String(20), nullable=True)
    max_salary = Column(String(20), nullable=True)
    currency = Column(String(3), default="USD")
    salary_period = Column(SQLEnum(SalaryPeriod), default=SalaryPeriod.YEARLY)
    
    # Experience & Company
    experience_level = Column(JSON, default=list)  # entry, mid, senior, etc.
    company_size = Column(JSON, default=list)  # startup, small, medium, large
    
    # Relocation & Visa
    willing_to_relocate = Column(Boolean, default=False)
    require_visa_sponsorship = Column(Boolean, default=False)
    
    # Application Settings
    auto_apply = Column(Boolean, default=False)
    daily_swipe_limit = Column(String(20), default="50")
    search_radius = Column(String(20), default="50")  # in miles/km
    
    # Notifications
    notification_settings = Column(JSON, default={
        "email": {
            "new_matches": True,
            "application_updates": True,
            "recommendations": True,
            "weekly_digest": True
        },
        "push": {
            "new_matches": True,
            "application_updates": True,
            "recommendations": False
        }
    })
    
    # Relationships
    user = relationship("User", back_populates="preferences")
