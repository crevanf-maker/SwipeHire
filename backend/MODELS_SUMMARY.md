# SwipeHire Database Models Summary

## 📊 Complete List of Models (20 Total)

### 🔐 Authentication & User Management (3 models)

1. **User** (`users`)
   - Core user account with OAuth support
   - Fields: email, password_hash, first_name, last_name, phone, account_type, oauth_provider
   - Supports: Google, LinkedIn, GitHub, Facebook OAuth
   - Includes: email verification, phone verification, soft delete

2. **UserSession** (`user_sessions`)
   - JWT session management
   - Fields: token, refresh_token, device_info, ip_address, expires_at
   - Tracks: device type, browser, location, activity

3. **UserPreferences** (`user_preferences`)
   - Job search preferences
   - Fields: preferred_job_titles, locations, industries, salary range
   - Settings: auto_apply, notification_settings, daily_swipe_limit
   - Work preferences: remote/hybrid/onsite, relocation, visa sponsorship

### 👤 User Profile (6 models)

4. **Profile** (`profiles`)
   - Professional profile
   - Fields: headline, summary, current_position, total_experience
   - Location: city, state, country, lat/long
   - Social: LinkedIn, GitHub, portfolio URLs
   - Status: profile completion %, open to opportunities

5. **Skill** (`skills`)
   - User skills with proficiency
   - Fields: skill_name, category, proficiency_level (beginner to expert)
   - Categories: programming, framework, database, cloud, tools, soft skills
   - Tracking: years of experience, is_verified, endorsements

6. **Experience** (`experiences`)
   - Work history
   - Fields: job_title, company, employment_type, dates
   - Details: achievements array, technologies_used array
   - Additional: team_size, reporting_to, remote status

7. **Education** (`educations`)
   - Educational background
   - Fields: institution, degree_type, field_of_study, grades
   - Types: high school to doctorate, bootcamps, certifications
   - Details: honors, relevant coursework, activities

8. **Certification** (`certifications`)
   - Professional certifications
   - Fields: name, issuing_org, credential_id, expiry_date
   - Tracking: is_verified, skills_acquired
   - Links: credential_url for verification

9. **Language** (`languages`)
   - Language proficiency
   - Fields: language_name, proficiency_level (elementary to native)
   - Abilities: can_read, can_write, can_speak

### 🏢 Companies & Jobs (3 models)

10. **Company** (`companies`)
    - Company profiles
    - Fields: name, logo, description, industry, company_size
    - Details: culture_values, tech_stack, benefits, perks
    - Funding: funding_stage, total_funding_amount
    - Stats: rating, reviews, glassdoor_rating, employee count
    - Status: is_verified, is_hiring, is_featured

11. **Job** (`jobs`)
    - Job postings
    - Fields: title, description, responsibilities, requirements
    - Employment: type, work_mode, experience_level, education_level
    - Location: city, state, country, lat/long, is_remote
    - Salary: min/max, currency, period, show_salary
    - Benefits: equity, benefits array, perks array
    - Requirements: visa_sponsorship, relocation_assistance
    - Status: job_status (draft, active, paused, filled, closed)
    - Stats: view_count, application_count, swipe counts
    - Timeline: application_deadline, start_date, published_at

12. **JobSkill** (`job_skills`)
    - Required skills for jobs
    - Fields: skill_name, category, importance (required/preferred/nice-to-have)
    - Details: proficiency_required, years_required, weight for matching

### 📱 Swiping & Applications (3 models)

13. **Swipe** (`swipes`)
    - Tinder-style swipe tracking
    - Direction: left (skip), right (interested), super (very interested)
    - Analytics: time_spent_viewing, device_type, session_id
    - Context: swipe_context (filters applied, source)
    - Application: auto_applied flag, match_score at swipe

14. **Application** (`applications`)
    - Job applications
    - Status: 9 stages (pending → accepted/rejected)
    - Method: auto_swipe, manual, quick_apply, external
    - Timeline: submitted_at, viewed_by_employer_at, status updates
    - Details: expected_salary, available_from, notice_period
    - Interview: scheduled_at, interview_type, interview_details
    - Offer: offer_details JSON
    - Feedback: rejection_reason, feedback, user_rating

15. **SavedJob** (`saved_jobs`)
    - Bookmarked jobs
    - Organization: folder_name, tags array, notes
    - Reminders: reminder_date, is_notified

### 🤖 AI Features (5 models)

16. **Resume** (`resumes`)
    - AI-generated resumes
    - Generation: is_ai_generated, generation_prompt, ai_model_version
    - Targeting: target_job_title, target_industry
    - Content: content_sections (JSON), formatting_options
    - File: file_url, format (PDF/DOCX/TXT/HTML), size, page_count
    - ATS: ats_score, ats_analysis, keywords_included
    - Versioning: version_number, parent_resume_id
    - Stats: view_count, download_count, application_count

17. **CoverLetter** (`cover_letters`)
    - AI-generated cover letters
    - Generation: is_ai_generated, tone (professional/friendly/enthusiastic)
    - Content: title, content, word_count
    - Personalization: personalization_data (JSON)
    - Usage: application_count, last_used_at

18. **AIRecommendation** (`ai_recommendations`)
    - AI job recommendations
    - Scores: recommendation_score, match_percentage
    - Component scores: skill, experience, location, salary, culture match
    - Explanation: recommendation_reason, matching/missing skills
    - Feedback: strength_points, improvement_suggestions
    - Type: perfect_match, high_match, good_match, potential_match, stretch_role
    - Display: is_shown, shown_at, rank

19. **MatchScore** (`match_scores`)
    - Detailed job match scoring
    - Overall: overall_score (0-100)
    - 9 Component Scores:
      - skills_score (30% weight)
      - experience_score (25%)
      - education_score (10%)
      - location_score (10%)
      - salary_score (10%)
      - job_type_score (5%)
      - industry_score (5%)
      - company_culture_score (3%)
      - career_growth_score (2%)
    - Analysis: detailed_breakdown, matched_skills_count, missing_critical_skills
    - Maintenance: calculation_version, last_calculated_at, is_stale

## 🔗 Key Relationships

```
User (1) → (1) Profile
User (1) → (1) UserPreferences
User (1) → (*) Skills, Experiences, Education, Certifications, Languages
User (1) → (*) Swipes, Applications, SavedJobs
User (1) → (*) Resumes, CoverLetters
User (1) → (*) AIRecommendations, MatchScores

Company (1) → (*) Jobs
Job (1) → (*) JobSkills
Job (1) → (*) Swipes, Applications, SavedJobs
Job (1) → (*) AIRecommendations, MatchScores

Application → Resume (reference)
Application → CoverLetter (reference)
Application → Swipe (reference)
```

## 📈 Statistics

- **Total Models**: 20
- **Enums**: 25+ enum types for data consistency
- **JSON Fields**: 15+ JSONB columns for flexible data
- **Array Fields**: 30+ array columns
- **Indexes**: 100+ indexes for performance
- **UUID Primary Keys**: All models use UUID for security
- **Soft Deletes**: 14 models support soft delete
- **Timestamps**: All models have created_at/updated_at

## 🎯 Key Features

1. **Tinder-Style Swiping**
   - Track all swipes with analytics
   - Auto-apply on right swipe (optional)
   - Super swipe for premium interest

2. **AI-Powered Matching**
   - 9-factor weighted algorithm
   - Real-time recommendations
   - Skills gap analysis

3. **Smart Application Management**
   - 9-stage status tracking
   - Interview scheduling
   - Offer management
   - Application analytics

4. **AI Resume Generation**
   - Multiple resume versions
   - ATS score analysis
   - Job-specific tailoring
   - Version control

5. **Comprehensive Profiles**
   - Skills with proficiency
   - Detailed work history
   - Education & certifications
   - Language proficiency

6. **Advanced Search**
   - Location-based (lat/long)
   - Salary filtering
   - Skills matching
   - Company preferences

## 🔒 Security Features

- UUID primary keys (not sequential IDs)
- Password hashing with bcrypt
- JWT session management
- Soft deletes for data recovery
- OAuth 2.0 support
- Device tracking

## 📱 Flutter Integration Ready

All models are designed for easy Flutter integration:
- RESTful API endpoints
- JSON serialization
- Pagination support
- Real-time updates ready
- Image URL storage (AWS S3 compatible)

## 🚀 Performance Optimizations

- Strategic indexes on all foreign keys
- Composite indexes for common queries
- JSONB for flexible data without schema changes
- Efficient relationship loading
- Query optimization ready
