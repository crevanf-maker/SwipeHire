from sqlalchemy import Column, String, Boolean, ForeignKey, Text, Enum as SQLEnum, DateTime, Integer, DECIMAL, JSON
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel, SoftDeleteMixin


class SwipeDirection(str, enum.Enum):
    LEFT = "left"  # Skip
    RIGHT = "right"  # Interested
    SUPER = "super"  # Very interested


class DeviceType(str, enum.Enum):
    MOBILE = "mobile"
    TABLET = "tablet"
    DESKTOP = "desktop"


class Swipe(BaseModel):
    __tablename__ = "swipes"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_id = Column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    
    swipe_direction = Column(SQLEnum(SwipeDirection), nullable=False, index=True)
    swipe_timestamp = Column(DateTime(timezone=True), server_default=None, nullable=False)
    
    # Analytics
    time_spent_viewing = Column(Integer, nullable=True)  # in seconds
    device_type = Column(SQLEnum(DeviceType), nullable=True)
    session_id = Column(String(36), nullable=True, index=True)
    swipe_context = Column(JSON, default=dict)
    
    # Application
    auto_applied = Column(Boolean, default=False)
    match_score = Column(DECIMAL(5, 2), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="swipes")
    job = relationship("Job", back_populates="swipes")


class ApplicationStatus(str, enum.Enum):
    PENDING = "pending"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    SHORTLISTED = "shortlisted"
    INTERVIEWING = "interviewing"
    OFFER_RECEIVED = "offer_received"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


class ApplicationMethod(str, enum.Enum):
    AUTO_SWIPE = "auto_swipe"
    MANUAL = "manual"
    QUICK_APPLY = "quick_apply"
    EXTERNAL = "external"


class InterviewType(str, enum.Enum):
    PHONE = "phone"
    VIDEO = "video"
    ONSITE = "onsite"
    TECHNICAL = "technical"
    HR = "hr"
    FINAL = "final"
    OTHER = "other"


class Application(BaseModel, SoftDeleteMixin):
    __tablename__ = "applications"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_id = Column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    swipe_id = Column(String(36), ForeignKey("swipes.id"), nullable=True)
    resume_id = Column(String(36), ForeignKey("resumes.id"), nullable=True)
    cover_letter_id = Column(String(36), ForeignKey("cover_letters.id"), nullable=True)
    
    # Status
    application_status = Column(SQLEnum(ApplicationStatus), default=ApplicationStatus.PENDING, index=True)
    current_stage = Column(String(100), nullable=True)
    application_method = Column(SQLEnum(ApplicationMethod), default=ApplicationMethod.AUTO_SWIPE)
    is_auto_applied = Column(Boolean, default=False)
    
    # Timeline
    submitted_at = Column(DateTime(timezone=True), nullable=True, index=True)
    viewed_by_employer_at = Column(DateTime(timezone=True), nullable=True)
    last_status_update_at = Column(DateTime(timezone=True), server_default=None)
    
    # Salary & Availability
    expected_salary = Column(Integer, nullable=True)
    salary_currency = Column(String(3), default="USD")
    available_from = Column(DateTime(timezone=True), nullable=True)
    notice_period_days = Column(Integer, nullable=True)
    
    # Application Details
    screening_answers = Column(JSON, default=dict)
    additional_documents = Column(JSON, default=list)
    notes = Column(Text, nullable=True)
    employer_notes = Column(Text, nullable=True)
    
    # Feedback
    rejection_reason = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)
    rating_by_user = Column(Integer, nullable=True)  # 1-5
    
    # Interview
    interview_scheduled_at = Column(DateTime(timezone=True), nullable=True, index=True)
    interview_type = Column(SQLEnum(InterviewType), nullable=True)
    interview_details = Column(JSON, default=dict)
    
    # Offer
    offer_details = Column(JSON, default=dict)
    
    # External
    external_application_id = Column(String(255), nullable=True)
    external_status = Column(String(100), nullable=True)
    source = Column(String(100), default="swipehire")
    
    # User Actions
    is_favorite = Column(Boolean, default=False, index=True)
    match_score = Column(DECIMAL(5, 2), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")
    swipe = relationship("Swipe")
    resume = relationship("Resume")
    cover_letter = relationship("CoverLetter")


class SavedJob(BaseModel):
    __tablename__ = "saved_jobs"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_id = Column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Organization
    folder_name = Column(String(100), default="default", index=True)
    tags = Column(JSON, default=list)
    notes = Column(Text, nullable=True)
    
    # Reminder
    reminder_date = Column(DateTime(timezone=True), nullable=True, index=True)
    is_notified = Column(Boolean, default=False)
    
    saved_at = Column(DateTime(timezone=True), server_default="now()")
    
    # Relationships
    user = relationship("User", back_populates="saved_jobs")
    job = relationship("Job", back_populates="saved_by")
