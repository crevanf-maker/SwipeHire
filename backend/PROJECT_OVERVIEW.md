# SwipeHire - AI-Powered Job Application Platform

## 🎯 Project Overview

**SwipeHire** is an innovative job application platform that combines the intuitive swiping interface of Tinder with powerful AI features to revolutionize the job search experience. Built for job seekers to quickly discover and apply to relevant positions.

### Tech Stack

- **Backend**: Python 3.11+ with FastAPI
- **Database**: PostgreSQL 14+
- **ORM**: SQLAlchemy 2.0
- **Frontend**: Flutter (Mobile/Web/Desktop)
- **AI**: OpenAI GPT-4
- **Authentication**: JWT + OAuth 2.0

## ✨ Core Features

### 1. **Tinder-Style Job Swiping** 🎯
- **Left Swipe**: Skip job
- **Right Swipe**: Show interest (auto-apply option)
- **Super Swipe**: Very interested (premium feature)
- Real-time match notifications
- Swipe analytics & insights

### 2. **AI-Powered Features** 🤖

#### Resume Generation
- AI-generated resumes tailored to specific jobs
- Multiple resume versions
- ATS (Applicant Tracking System) score analysis
- Professional templates
- Export to PDF/DOCX

#### Cover Letter Generation
- Job-specific personalized cover letters
- Multiple tone options (professional, friendly, enthusiastic)
- AI-powered content optimization
- Template-based formatting

#### Smart Job Matching
- 9-factor weighted algorithm:
  - Skills Match (30%)
  - Experience Level (25%)
  - Education (10%)
  - Location (10%)
  - Salary (10%)
  - Job Type (5%)
  - Industry (5%)
  - Company Culture (3%)
  - Career Growth (2%)

#### Intelligent Recommendations
- Perfect match, high match, good match categories
- Skill gap analysis
- Strength points identification
- Improvement suggestions
- Personalized explanations

### 3. **Comprehensive Profile Management** 👤
- Professional headline & summary
- Skills with proficiency levels (beginner to expert)
- Work experience history with achievements
- Education background
- Professional certifications (with verification)
- Language proficiency
- Portfolio & social media links

### 4. **Application Management** 📋
- Track applications through 9 stages:
  1. Pending
  2. Submitted
  3. Under Review
  4. Shortlisted
  5. Interviewing
  6. Offer Received
  7. Accepted
  8. Rejected
  9. Withdrawn
- Interview scheduling & tracking
- Offer management
- Application notes & reminders
- Status notifications

### 5. **Advanced Search & Discovery** 🔍
- Location-based search (with radius)
- Salary filtering
- Company size & type preferences
- Work mode (remote/hybrid/onsite)
- Industry & job category filters
- Skills-based matching
- Save jobs to custom folders

### 6. **Company Profiles** 🏢
- Detailed company information
- Culture & values
- Tech stack & tools used
- Benefits & perks
- Office locations
- Funding stage & growth stats
- Employee reviews & ratings

## 📊 Database Architecture

### 20 Main Models

**User & Auth (3)**
- Users with OAuth
- Sessions (JWT)
- User Preferences

**Profile (6)**
- Profile
- Skills
- Experience
- Education
- Certifications
- Languages

**Jobs (3)**
- Companies
- Jobs
- Job Skills

**Applications (3)**
- Swipes
- Applications
- Saved Jobs

**AI Features (5)**
- Resumes
- Cover Letters
- AI Recommendations
- Match Scores

### Key Statistics
- **Total Models**: 20
- **Enum Types**: 25+
- **JSON Fields**: 15+ (for flexibility)
- **Array Fields**: 30+
- **Indexes**: 100+ (optimized for performance)
- **Soft Deletes**: 14 models

## 🚀 Getting Started

### Prerequisites
```bash
- Python 3.11+
- PostgreSQL 14+
- pip or poetry
```

### Quick Setup
```bash
# 1. Clone and navigate
cd SwipeHire/backend

# 2. Run setup script
python setup.py

# 3. Configure environment
cp env.example .env
# Edit .env with your settings

# 4. Create database
createdb swipehire_dev

# 5. Initialize tables
python init_db.py

# 6. Start server
python main.py

# 7. Access API docs
open http://localhost:8000/docs
```

### Manual Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Setup database
createdb swipehire_dev
python init_db.py

# Run server
uvicorn main:app --reload
```

## 📱 API Endpoints (For Flutter)

### Authentication
```
POST   /api/v1/auth/register          - Register user
POST   /api/v1/auth/login             - Login
POST   /api/v1/auth/refresh           - Refresh token
POST   /api/v1/auth/logout            - Logout
GET    /api/v1/auth/oauth/{provider}  - OAuth login
```

### Profile
```
GET    /api/v1/profile                - Get profile
PUT    /api/v1/profile                - Update profile
POST   /api/v1/skills                 - Add skill
POST   /api/v1/experience             - Add experience
POST   /api/v1/education              - Add education
```

### Job Swiping
```
GET    /api/v1/jobs/feed              - Get swipeable jobs
POST   /api/v1/swipes                 - Record swipe
GET    /api/v1/swipes/history         - Swipe history
GET    /api/v1/swipes/analytics       - User swipe analytics
```

### Applications
```
POST   /api/v1/applications           - Apply to job
GET    /api/v1/applications           - List applications
GET    /api/v1/applications/{id}      - Get application
PUT    /api/v1/applications/{id}      - Update application
DELETE /api/v1/applications/{id}      - Withdraw application
```

### AI Features
```
POST   /api/v1/ai/resume/generate     - Generate AI resume
POST   /api/v1/ai/cover-letter/generate - Generate cover letter
GET    /api/v1/ai/recommendations     - Get job recommendations
GET    /api/v1/ai/match-score/{job_id} - Get match score
POST   /api/v1/ai/resume/analyze      - Analyze resume ATS score
```

### Search & Discovery
```
GET    /api/v1/jobs/search            - Search jobs
GET    /api/v1/jobs/{id}              - Get job details
GET    /api/v1/companies              - List companies
GET    /api/v1/companies/{id}         - Company details
POST   /api/v1/saved-jobs             - Save job
GET    /api/v1/saved-jobs             - List saved jobs
```

## 🔒 Security Features

- **Password Security**: bcrypt hashing
- **JWT Authentication**: Access & refresh tokens (24h + 30d)
- **OAuth 2.0**: Google, LinkedIn, GitHub, Facebook
- **Session Management**: Device & location tracking
- **UUID Keys**: Non-sequential IDs for security
- **Soft Deletes**: Data recovery capability
- **CORS**: Configured for Flutter apps
- **Rate Limiting**: API abuse prevention

## 🎨 Flutter Integration Example

```dart
// Swipe on a job
Future<void> swipeJob(String jobId, String direction) async {
  final response = await http.post(
    Uri.parse('$baseUrl/api/v1/swipes'),
    headers: {
      'Authorization': 'Bearer $token',
      'Content-Type': 'application/json',
    },
    body: jsonEncode({
      'job_id': jobId,
      'direction': direction,  // 'left', 'right', 'super'
      'auto_apply': true,      // Auto-apply on right swipe
      'time_spent_viewing': 45 // seconds
    }),
  );
  
  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    if (data['auto_applied']) {
      // Show success notification
    }
  }
}

// Generate AI resume
Future<Resume> generateResume(String targetJobTitle) async {
  final response = await http.post(
    Uri.parse('$baseUrl/api/v1/ai/resume/generate'),
    headers: {
      'Authorization': 'Bearer $token',
      'Content-Type': 'application/json',
    },
    body: jsonEncode({
      'target_job_title': targetJobTitle,
      'target_industry': 'Technology',
      'template_id': 'modern-professional'
    }),
  );
  
  return Resume.fromJson(jsonDecode(response.body)['data']);
}

// Get job recommendations
Future<List<JobRecommendation>> getRecommendations() async {
  final response = await http.get(
    Uri.parse('$baseUrl/api/v1/ai/recommendations?limit=20'),
    headers: {'Authorization': 'Bearer $token'},
  );
  
  final data = jsonDecode(response.body)['data'];
  return (data as List)
      .map((json) => JobRecommendation.fromJson(json))
      .toList();
}
```

## 📈 Scalability & Performance

- **Database Indexing**: 100+ strategic indexes
- **Query Optimization**: Efficient joins & relationships
- **Caching Ready**: Redis integration support
- **Async Operations**: FastAPI async/await
- **Connection Pooling**: SQLAlchemy pool management
- **Pagination**: Efficient data loading
- **File Storage**: AWS S3 ready
- **Background Jobs**: Celery integration ready

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=app --cov-report=html

# Specific test
pytest tests/test_swipes.py
```

## 🚢 Deployment

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Commands
```bash
# Using Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Database migrations
alembic upgrade head

# Environment
export DATABASE_URL="postgresql://..."
export SECRET_KEY="..."
```

## 📚 Documentation

- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **Database Schema**: `DATABASE_SCHEMA.md`
- **Models Summary**: `MODELS_SUMMARY.md`
- **README**: `README.md`

## 🤝 Contributing

1. Follow PEP 8 style guide
2. Write tests for new features
3. Use type hints
4. Format with Black: `black app/`
5. Lint with Flake8: `flake8 app/`
6. Update documentation

## 📄 Project Structure

```
SwipeHire/backend/
├── app/
│   ├── models/          # SQLAlchemy models (20 models)
│   ├── api/v1/          # API endpoints
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic
│   ├── core/            # Config & database
│   └── utils/           # Utilities
├── alembic/             # Database migrations
├── tests/               # Unit & integration tests
├── main.py              # FastAPI app
├── init_db.py           # DB initialization
├── setup.py             # Quick setup script
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## 🎯 Roadmap

- [ ] Implement all API endpoints
- [ ] Add real-time notifications (WebSocket)
- [ ] Implement AI recommendation engine
- [ ] Add email notifications
- [ ] Create admin dashboard
- [ ] Add analytics & insights
- [ ] Implement chat with recruiters
- [ ] Add video interview scheduling
- [ ] Create mobile app (Flutter)
- [ ] Add premium features

## 📞 Support

- **Documentation**: `/docs` endpoint
- **Email**: support@swipehire.com
- **Issues**: GitHub Issues

## 📝 License

MIT License

---

Built with ❤️ by SwipeHire Team

**Happy Job Hunting! 🎉**
