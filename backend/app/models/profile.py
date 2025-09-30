from sqlalchemy import Column, String, Boolean, ForeignKey, Text, Enum as SQLEnum, Date, DECIMAL, Integer, JSON
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel, SoftDeleteMixin


class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


class Availability(str, enum.Enum):
    IMMEDIATE = "immediate"
    WITHIN_2_WEEKS = "within_2_weeks"
    WITHIN_1_MONTH = "within_1_month"
    WITHIN_3_MONTHS = "within_3_months"
    NOT_LOOKING = "not_looking"


class Profile(BaseModel, SoftDeleteMixin):
    __tablename__ = "profiles"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    
    # Professional Info
    headline = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)
    current_position = Column(String(255), nullable=True)
    current_company = Column(String(255), nullable=True)
    total_experience_years = Column(DECIMAL(4, 1), default=0)
    
    # Personal Info
    date_of_birth = Column(Date, nullable=True)
    gender = Column(SQLEnum(Gender), nullable=True)
    
    # Location
    location_city = Column(String(100), nullable=True, index=True)
    location_state = Column(String(100), nullable=True, index=True)
    location_country = Column(String(100), nullable=True, index=True)
    location_zip = Column(String(20), nullable=True)
    latitude = Column(DECIMAL(10, 8), nullable=True)
    longitude = Column(DECIMAL(11, 8), nullable=True)
    
    # Links
    website_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    github_url = Column(String(255), nullable=True)
    portfolio_url = Column(String(255), nullable=True)
    resume_url = Column(Text, nullable=True)
    
    # Profile Status
    is_profile_complete = Column(Boolean, default=False)
    profile_completion_percentage = Column(Integer, default=0)
    is_profile_public = Column(Boolean, default=True)
    is_open_to_opportunities = Column(Boolean, default=True, index=True)
    
    # Availability
    availability = Column(SQLEnum(Availability), default=Availability.WITHIN_1_MONTH)
    notice_period_days = Column(Integer, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="profile")


class ProficiencyLevel(str, enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class SkillCategory(str, enum.Enum):
    PROGRAMMING_LANGUAGE = "programming_language"
    FRAMEWORK = "framework"
    DATABASE = "database"
    CLOUD_PLATFORM = "cloud_platform"
    TOOL = "tool"
    SOFT_SKILL = "soft_skill"
    LANGUAGE = "language"
    METHODOLOGY = "methodology"
    DOMAIN_KNOWLEDGE = "domain_knowledge"
    OTHER = "other"


class Skill(BaseModel, SoftDeleteMixin):
    __tablename__ = "skills"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_name = Column(String(100), nullable=False, index=True)
    skill_category = Column(SQLEnum(SkillCategory), default=SkillCategory.OTHER)
    proficiency_level = Column(SQLEnum(ProficiencyLevel), default=ProficiencyLevel.INTERMEDIATE)
    years_of_experience = Column(DECIMAL(4, 1), nullable=True)
    
    is_primary_skill = Column(Boolean, default=False, index=True)
    is_verified = Column(Boolean, default=False)
    endorsement_count = Column(Integer, default=0)
    last_used = Column(Date, nullable=True)
    display_order = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="skills")


class EmploymentType(str, enum.Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"
    VOLUNTEER = "volunteer"


class Experience(BaseModel, SoftDeleteMixin):
    __tablename__ = "experiences"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    job_title = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False, index=True)
    company_logo_url = Column(Text, nullable=True)
    employment_type = Column(SQLEnum(EmploymentType), default=EmploymentType.FULL_TIME)
    
    location = Column(String(255), nullable=True)
    is_remote = Column(Boolean, default=False)
    
    start_date = Column(Date, nullable=False, index=True)
    end_date = Column(Date, nullable=True)
    is_current = Column(Boolean, default=False, index=True)
    
    description = Column(Text, nullable=True)
    achievements = Column(JSON, default=list)
    technologies_used = Column(JSON, default=list)
    
    industry = Column(String(100), nullable=True)
    team_size = Column(Integer, nullable=True)
    reporting_to = Column(String(255), nullable=True)
    display_order = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="experiences")


class DegreeType(str, enum.Enum):
    HIGH_SCHOOL = "high_school"
    ASSOCIATE = "associate"
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTORATE = "doctorate"
    CERTIFICATION = "certification"
    BOOTCAMP = "bootcamp"
    DIPLOMA = "diploma"
    OTHER = "other"


class GradeType(str, enum.Enum):
    GPA = "gpa"
    PERCENTAGE = "percentage"
    CGPA = "cgpa"
    GRADE = "grade"
    NONE = "none"


class Education(BaseModel, SoftDeleteMixin):
    __tablename__ = "educations"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    institution_name = Column(String(255), nullable=False, index=True)
    institution_logo_url = Column(Text, nullable=True)
    degree_type = Column(SQLEnum(DegreeType), nullable=False, index=True)
    field_of_study = Column(String(255), nullable=True)
    degree_name = Column(String(255), nullable=True)
    
    grade_type = Column(SQLEnum(GradeType), default=GradeType.NONE)
    grade_value = Column(String(20), nullable=True)
    grade_scale = Column(String(20), nullable=True)
    
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    is_current = Column(Boolean, default=False, index=True)
    
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    activities = Column(Text, nullable=True)
    honors_awards = Column(JSON, default=list)
    relevant_coursework = Column(JSON, default=list)
    display_order = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="education")


class Certification(BaseModel, SoftDeleteMixin):
    __tablename__ = "certifications"
    
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    certification_name = Column(String(255), nullable=False)
    issuing_organization = Column(String(255), nullable=False, index=True)
    organization_logo_url = Column(Text, nullable=True)
    credential_id = Column(String(255), nullable=True)
    credential_url = Column(Text, nullable=True)
    
    issue_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True, index=True)
    does_not_expire = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    
    description = Column(Text, nullable=True)
    skills_acquired = Column(ARRAY(String), default=list)
    display_order = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="certifications")


class LanguageProficiency(str, enum.Enum):
    ELEMENTARY = "elementary"
    LIMITED_WORKING = "limited_working"
    PROFESSIONAL_WORKING = "professional_working"
    FULL_PROFESSIONAL = "full_professional"
    NATIVE = "native"


class Language(BaseModel, SoftDeleteMixin):
    __tablename__ = "languages"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    language_name = Column(String(100), nullable=False, index=True)
    language_code = Column(String(10), nullable=True)
    proficiency_level = Column(SQLEnum(LanguageProficiency), nullable=False)
    
    can_read = Column(Boolean, default=True)
    can_write = Column(Boolean, default=True)
    can_speak = Column(Boolean, default=True)
    is_native = Column(Boolean, default=False)
    display_order = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="languages")
