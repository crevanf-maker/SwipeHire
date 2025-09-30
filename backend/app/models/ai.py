from sqlalchemy import Column, String, Boolean, ForeignKey, Text, Enum as SQLEnum, DateTime, Integer, DECIMAL, JSON
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel, SoftDeleteMixin


class FileFormat(str, enum.Enum):
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    HTML = "html"


class Resume(BaseModel, SoftDeleteMixin):
    __tablename__ = "resumes"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Basic Info
    resume_name = Column(String(255), nullable=False)
    template_id = Column(String(100), nullable=True)
    
    # AI Generation
    is_ai_generated = Column(Boolean, default=False, index=True)
    generation_prompt = Column(Text, nullable=True)
    ai_model_version = Column(String(50), nullable=True)
    
    # Targeting
    target_job_title = Column(String(255), nullable=True)
    target_industry = Column(String(100), nullable=True)
    
    # Content
    content_sections = Column(JSON, default=dict)
    formatting_options = Column(JSON, default=dict)
    
    # File
    file_url = Column(Text, nullable=True)
    file_format = Column(SQLEnum(FileFormat), default=FileFormat.PDF)
    file_size_bytes = Column(Integer, nullable=True)
    page_count = Column(Integer, default=1)
    word_count = Column(Integer, nullable=True)
    
    # Status
    is_default = Column(Boolean, default=False, index=True)
    is_public = Column(Boolean, default=False)
    public_url = Column(String(255), nullable=True, unique=True)
    
    # Stats
    view_count = Column(Integer, default=0)
    download_count = Column(Integer, default=0)
    application_count = Column(Integer, default=0)
    
    # ATS Analysis
    ats_score = Column(DECIMAL(5, 2), nullable=True)
    ats_analysis = Column(JSON, default=dict)
    keywords_included = Column(JSON, default=list)
    
    # Versioning
    last_used_at = Column(DateTime(timezone=True), nullable=True)
    version_number = Column(Integer, default=1)
    parent_resume_id = Column(String(36), ForeignKey("resumes.id"), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="resumes")
    versions = relationship("Resume", backref="parent", remote_side="Resume.id")


class CoverLetterTone(str, enum.Enum):
    PROFESSIONAL = "professional"
    FRIENDLY = "friendly"
    ENTHUSIASTIC = "enthusiastic"
    FORMAL = "formal"
    CREATIVE = "creative"


class CoverLetter(BaseModel, SoftDeleteMixin):
    __tablename__ = "cover_letters"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_id = Column(String(36), ForeignKey("jobs.id"), nullable=True, index=True)
    
    # Basic Info
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    
    # AI Generation
    is_ai_generated = Column(Boolean, default=False, index=True)
    generation_prompt = Column(Text, nullable=True)
    ai_model_version = Column(String(50), nullable=True)
    tone = Column(SQLEnum(CoverLetterTone), default=CoverLetterTone.PROFESSIONAL)
    
    # Template & Personalization
    template_id = Column(String(100), nullable=True)
    personalization_data = Column(JSON, default=dict)
    
    # File
    file_url = Column(Text, nullable=True)
    word_count = Column(Integer, nullable=True)
    
    # Status
    is_default = Column(Boolean, default=False, index=True)
    application_count = Column(Integer, default=0)
    last_used_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="cover_letters")
    job = relationship("Job", back_populates="cover_letters")


class RecommendationType(str, enum.Enum):
    PERFECT_MATCH = "perfect_match"
    HIGH_MATCH = "high_match"
    GOOD_MATCH = "good_match"
    POTENTIAL_MATCH = "potential_match"
    STRETCH_ROLE = "stretch_role"


class AIRecommendation(BaseModel):
    __tablename__ = "ai_recommendations"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_id = Column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Scores
    recommendation_score = Column(DECIMAL(5, 2), nullable=False, index=True)
    match_percentage = Column(DECIMAL(5, 2), nullable=False, index=True)
    skill_match_score = Column(DECIMAL(5, 2), nullable=True)
    experience_match_score = Column(DECIMAL(5, 2), nullable=True)
    location_match_score = Column(DECIMAL(5, 2), nullable=True)
    salary_match_score = Column(DECIMAL(5, 2), nullable=True)
    culture_match_score = Column(DECIMAL(5, 2), nullable=True)
    
    # Explanation
    recommendation_reason = Column(Text, nullable=True)
    matching_skills = Column(JSON, default=list)
    missing_skills = Column(JSON, default=list)
    strength_points = Column(JSON, default=list)
    improvement_suggestions = Column(JSON, default=list)
    
    # Classification
    recommendation_type = Column(SQLEnum(RecommendationType), nullable=False, index=True)
    
    # AI Metadata
    algorithm_version = Column(String(50), nullable=True)
    model_metadata = Column(JSON, default=dict)
    
    # Display
    is_shown = Column(Boolean, default=False, index=True)
    shown_at = Column(DateTime(timezone=True), nullable=True)
    rank = Column(Integer, nullable=True, index=True)
    
    # Relationships
    user = relationship("User", back_populates="recommendations")
    job = relationship("Job", back_populates="recommendations")


class MatchScore(BaseModel):
    __tablename__ = "match_scores"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_id = Column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Overall Score
    overall_score = Column(DECIMAL(5, 2), nullable=False, index=True)
    
    # Component Scores
    skills_score = Column(DECIMAL(5, 2), default=0)
    experience_score = Column(DECIMAL(5, 2), default=0)
    education_score = Column(DECIMAL(5, 2), default=0)
    location_score = Column(DECIMAL(5, 2), default=0)
    salary_score = Column(DECIMAL(5, 2), default=0)
    job_type_score = Column(DECIMAL(5, 2), default=0)
    industry_score = Column(DECIMAL(5, 2), default=0)
    company_culture_score = Column(DECIMAL(5, 2), default=0)
    career_growth_score = Column(DECIMAL(5, 2), default=0)
    
    # Weights
    weights = Column(JSON, default={
        "skills": 0.30,
        "experience": 0.25,
        "education": 0.10,
        "location": 0.10,
        "salary": 0.10,
        "job_type": 0.05,
        "industry": 0.05,
        "company_culture": 0.03,
        "career_growth": 0.02
    })
    
    # Detailed Analysis
    detailed_breakdown = Column(JSON, default=dict)
    matched_skills_count = Column(Integer, default=0)
    total_required_skills = Column(Integer, default=0)
    missing_critical_skills = Column(JSON, default=list)
    
    # Metadata
    calculation_version = Column(String(50), default="1.0")
    last_calculated_at = Column(DateTime(timezone=True), server_default=None)
    is_stale = Column(Boolean, default=False, index=True)
    
    # Relationships
    user = relationship("User", back_populates="match_scores")
    job = relationship("Job", back_populates="match_scores")
