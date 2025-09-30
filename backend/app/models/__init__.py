from app.models.base import BaseModel, SoftDeleteMixin
from app.models.user import User, AccountType, OAuthProvider
from app.models.auth import UserSession, UserPreferences, SalaryPeriod
from app.models.profile import (
    Profile, Gender, Availability,
    Skill, SkillCategory, ProficiencyLevel,
    Experience, EmploymentType,
    Education, DegreeType, GradeType,
    Certification,
    Language, LanguageProficiency
)
from app.models.job import (
    Company, CompanyType, FundingStage,
    Job, JobStatus, WorkMode, ExperienceLevel, EducationLevel, ApplyType, JobSource,
    JobSkill, SkillImportance
)
from app.models.application import (
    Swipe, SwipeDirection, DeviceType,
    Application, ApplicationStatus, ApplicationMethod, InterviewType,
    SavedJob
)
from app.models.ai import (
    Resume, FileFormat,
    CoverLetter, CoverLetterTone,
    AIRecommendation, RecommendationType,
    MatchScore
)

__all__ = [
    # Base
    "BaseModel",
    "SoftDeleteMixin",
    
    # User & Auth
    "User",
    "AccountType",
    "OAuthProvider",
    "UserSession",
    "UserPreferences",
    "SalaryPeriod",
    
    # Profile
    "Profile",
    "Gender",
    "Availability",
    "Skill",
    "SkillCategory",
    "ProficiencyLevel",
    "Experience",
    "EmploymentType",
    "Education",
    "DegreeType",
    "GradeType",
    "Certification",
    "Language",
    "LanguageProficiency",
    
    # Job & Company
    "Company",
    "CompanyType",
    "FundingStage",
    "Job",
    "JobStatus",
    "WorkMode",
    "ExperienceLevel",
    "EducationLevel",
    "ApplyType",
    "JobSource",
    "JobSkill",
    "SkillImportance",
    
    # Application
    "Swipe",
    "SwipeDirection",
    "DeviceType",
    "Application",
    "ApplicationStatus",
    "ApplicationMethod",
    "InterviewType",
    "SavedJob",
    
    # AI
    "Resume",
    "FileFormat",
    "CoverLetter",
    "CoverLetterTone",
    "AIRecommendation",
    "RecommendationType",
    "MatchScore",
]
