# SwipeHire Database Schema

## Overview
This document outlines the MySQL database structure for SwipeHire - an AI-powered job application platform with Tinder-like interface.

**Tech Stack:**
- Backend: Python 3.11+ with FastAPI
- ORM: SQLAlchemy 2.0
- Database: MySQL 8.0+
- Frontend: Flutter

## Core Entities

### 1. **Users & Authentication**
- `users` - Core user accounts
- `user_sessions` - Active user sessions
- `user_preferences` - User job preferences and filters

### 2. **User Profile**
- `profiles` - User professional profiles
- `skills` - User skills with proficiency levels
- `experiences` - Work experience history
- `education` - Educational background
- `certifications` - Professional certifications
- `languages` - Language proficiency

### 3. **Jobs & Companies**
- `companies` - Company information
- `jobs` - Job postings
- `job_skills` - Required skills for jobs
- `job_benefits` - Benefits offered by jobs

### 4. **Application & Interaction**
- `swipes` - User swipe history (left/right)
- `applications` - Job applications (auto-submitted on right swipe)
- `application_status` - Application status tracking
- `saved_jobs` - Bookmarked jobs for later

### 5. **AI Features**
- `resumes` - AI-generated resumes
- `resume_versions` - Different resume versions
- `ai_recommendations` - AI job recommendations
- `match_scores` - AI-calculated job match scores
- `cover_letters` - AI-generated cover letters

### 6. **Analytics & Tracking**
- `user_activity` - User activity logs
- `job_views` - Job view tracking
- `application_analytics` - Application performance metrics

## Key Relationships

```
users (1) -----> (1) profiles
users (1) -----> (*) skills
users (1) -----> (*) experiences
users (1) -----> (*) education
users (1) -----> (*) swipes
users (1) -----> (*) applications
users (1) -----> (*) resumes
users (1) -----> (1) user_preferences

companies (1) -----> (*) jobs
jobs (1) -----> (*) job_skills
jobs (1) -----> (*) applications
jobs (1) -----> (*) swipes

users + jobs -----> (1) match_scores
applications (1) -----> (*) application_status
```

## Indexes Strategy

- Primary keys on all tables
- Foreign key indexes for join optimization
- Composite indexes on frequently queried combinations
- Full-text search indexes on job descriptions and titles
- GiST indexes for advanced search features

## Database Features

- **UUID (as 36-char strings)** for primary keys (security & scalability)
- **Timestamps** on all tables (created_at, updated_at)
- **Soft deletes** for critical data (deleted_at)
- **JSON** for flexible AI metadata storage
- **Triggers** for automatic timestamp updates
- **Row-level security** for multi-tenant isolation
