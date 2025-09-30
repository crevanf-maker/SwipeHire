from sqlalchemy import Column, String, Boolean, ForeignKey, Text, Enum as SQLEnum, Date, DECIMAL, Integer, DateTime, BIGINT, JSON
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel, SoftDeleteMixin


class CompanyType(str, enum.Enum):
    STARTUP = "startup"
    SMALL_BUSINESS = "small_business"
    CORPORATE = "corporate"
    ENTERPRISE = "enterprise"
    NONPROFIT = "nonprofit"
    GOVERNMENT = "government"
    OTHER = "other"


class FundingStage(str, enum.Enum):
    BOOTSTRAPPED = "bootstrapped"
    PRE_SEED = "pre_seed"
    SEED = "seed"
    SERIES_A = "series_a"
    SERIES_B = "series_b"
    SERIES_C = "series_c"
    SERIES_D_PLUS = "series_d+"
    IPO = "ipo"
    ACQUIRED = "acquired"
    PUBLIC = "public"


class Company(BaseModel, SoftDeleteMixin):
    __tablename__ = "companies"
    
    company_name = Column(String(255), nullable=False, index=True)
    company_slug = Column(String(255), unique=True, nullable=True, index=True)
    
    # Media
    logo_url = Column(Text, nullable=True)
    cover_image_url = Column(Text, nullable=True)
    
    # Links
    website_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    twitter_url = Column(String(255), nullable=True)
    
    # Company Info
    industry = Column(String(100), nullable=True, index=True)
    company_size = Column(String(50), nullable=True, index=True)
    founded_year = Column(Integer, nullable=True)
    company_type = Column(SQLEnum(CompanyType), default=CompanyType.CORPORATE)
    
    # Description
    description = Column(Text, nullable=True)
    mission_statement = Column(Text, nullable=True)
    culture_values = Column(JSON, default=list)
    
    # Location
    headquarters_location = Column(String(255), nullable=True)
    headquarters_city = Column(String(100), nullable=True, index=True)
    headquarters_state = Column(String(100), nullable=True)
    headquarters_country = Column(String(100), nullable=True, index=True)
    office_locations = Column(JSON, default=list)
    
    # Tech & Benefits
    tech_stack = Column(JSON, default=list)
    benefits = Column(JSON, default=list)
    perks = Column(JSON, default=dict)
    
    # Funding
    funding_stage = Column(SQLEnum(FundingStage), nullable=True)
    total_funding_amount = Column(BIGINT, nullable=True)
    
    # Stats
    rating = Column(DECIMAL(3, 2), default=0)
    total_reviews = Column(Integer, default=0)
    glassdoor_rating = Column(DECIMAL(3, 2), nullable=True)
    linkedin_followers = Column(Integer, default=0)
    total_employees = Column(Integer, nullable=True)
    growth_rate = Column(DECIMAL(5, 2), nullable=True)
    
    # Status
    is_verified = Column(Boolean, default=False, index=True)
    is_featured = Column(Boolean, default=False, index=True)
    is_hiring = Column(Boolean, default=True, index=True)
    
    # Additional Data
    diversity_stats = Column(JSON, default=dict)
    
    # Relationships
    jobs = relationship("Job", back_populates="company", cascade="all, delete-orphan")


class EmploymentType(str, enum.Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"
    TEMPORARY = "temporary"


class WorkMode(str, enum.Enum):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"


class ExperienceLevel(str, enum.Enum):
    ENTRY = "entry"
    MID = "mid"
    SENIOR = "senior"
    LEAD = "lead"
    EXECUTIVE = "executive"


class EducationLevel(str, enum.Enum):
    HIGH_SCHOOL = "high_school"
    ASSOCIATE = "associate"
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTORATE = "doctorate"
    ANY = "any"


class JobStatus(str, enum.Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    FILLED = "filled"
    CLOSED = "closed"
    EXPIRED = "expired"


class ApplyType(str, enum.Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"
    EMAIL = "email"


class JobSource(str, enum.Enum):
    INTERNAL = "internal"
    IMPORTED = "imported"
    SCRAPED = "scraped"
    API = "api"


class Job(BaseModel, SoftDeleteMixin):
    __tablename__ = "jobs"
    
    company_id = Column(String(36), ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Basic Info
    job_title = Column(String(255), nullable=False, index=True)
    job_slug = Column(String(255), nullable=True, index=True)
    job_description = Column(Text, nullable=False)
    
    # Job Details
    job_responsibilities = Column(JSON, default=list)
    job_requirements = Column(JSON, default=list)
    nice_to_have = Column(JSON, default=list)
    
    # Employment Details
    employment_type = Column(SQLEnum(EmploymentType), default=EmploymentType.FULL_TIME, index=True)
    work_mode = Column(SQLEnum(WorkMode), default=WorkMode.REMOTE, index=True)
    experience_level = Column(SQLEnum(ExperienceLevel), nullable=False, index=True)
    min_experience_years = Column(Integer, nullable=True)
    max_experience_years = Column(Integer, nullable=True)
    education_level = Column(SQLEnum(EducationLevel), default=EducationLevel.ANY)
    
    # Location
    location_city = Column(String(100), nullable=True, index=True)
    location_state = Column(String(100), nullable=True)
    location_country = Column(String(100), nullable=True, index=True)
    location_zip = Column(String(20), nullable=True)
    latitude = Column(DECIMAL(10, 8), nullable=True)
    longitude = Column(DECIMAL(11, 8), nullable=True)
    is_location_flexible = Column(Boolean, default=False)
    
    # Salary
    salary_min = Column(Integer, nullable=True)
    salary_max = Column(Integer, nullable=True)
    salary_currency = Column(String(3), default="USD")
    salary_period = Column(String(20), default="yearly")
    is_salary_negotiable = Column(Boolean, default=True)
    show_salary = Column(Boolean, default=True)
    
    # Equity & Benefits
    equity_offered = Column(Boolean, default=False)
    equity_details = Column(Text, nullable=True)
    benefits = Column(JSON, default=list)
    perks = Column(JSON, default=list)
    
    # Department & Category
    department = Column(String(100), nullable=True)
    category = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True, index=True)
    
    # Requirements
    visa_sponsorship = Column(Boolean, default=False, index=True)
    relocation_assistance = Column(Boolean, default=False)
    required_languages = Column(JSON, default=["English"])
    
    # Team & Reporting
    team_size = Column(Integer, nullable=True)
    reporting_to = Column(String(255), nullable=True)
    interview_process = Column(JSON, default=dict)
    
    # Timeline
    application_deadline = Column(DateTime(timezone=True), nullable=True, index=True)
    start_date = Column(Date, nullable=True)
    
    # Status
    job_status = Column(SQLEnum(JobStatus), default=JobStatus.ACTIVE, index=True)
    is_featured = Column(Boolean, default=False, index=True)
    is_urgent = Column(Boolean, default=False, index=True)
    
    # Stats
    view_count = Column(Integer, default=0)
    application_count = Column(Integer, default=0)
    swipe_right_count = Column(Integer, default=0)
    swipe_left_count = Column(Integer, default=0)
    
    # External
    external_job_id = Column(String(255), nullable=True)
    external_url = Column(Text, nullable=True)
    source = Column(SQLEnum(JobSource), default=JobSource.INTERNAL)
    apply_type = Column(SQLEnum(ApplyType), default=ApplyType.INTERNAL)
    apply_email = Column(String(255), nullable=True)
    
    # Screening & AI
    screening_questions = Column(JSON, default=list)
    ai_match_keywords = Column(JSON, default=list)
    
    # Publishing
    published_at = Column(DateTime(timezone=True), nullable=True, index=True)
    
    # Relationships
    company = relationship("Company", back_populates="jobs")
    required_skills = relationship("JobSkill", back_populates="job", cascade="all, delete-orphan")
    swipes = relationship("Swipe", back_populates="job", cascade="all, delete-orphan")
    applications = relationship("Application", back_populates="job", cascade="all, delete-orphan")
    saved_by = relationship("SavedJob", back_populates="job", cascade="all, delete-orphan")
    cover_letters = relationship("CoverLetter", back_populates="job")
    recommendations = relationship("AIRecommendation", back_populates="job", cascade="all, delete-orphan")
    match_scores = relationship("MatchScore", back_populates="job", cascade="all, delete-orphan")


class SkillImportance(str, enum.Enum):
    REQUIRED = "required"
    PREFERRED = "preferred"
    NICE_TO_HAVE = "nice_to_have"


class JobSkill(BaseModel):
    __tablename__ = "job_skills"
    
    job_id = Column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_name = Column(String(100), nullable=False, index=True)
    skill_category = Column(String(50), default="other")
    importance = Column(SQLEnum(SkillImportance), default=SkillImportance.REQUIRED, index=True)
    proficiency_required = Column(String(50), nullable=True)
    years_required = Column(DECIMAL(4, 1), nullable=True)
    weight = Column(Integer, default=1)
    
    # Relationships
    job = relationship("Job", back_populates="required_skills")
