# SwipeHire Backend (Python/FastAPI)

Backend API for SwipeHire - An AI-powered job application platform with Tinder-like swiping interface for Flutter frontend.

## 🏗️ Tech Stack

- **Framework**: FastAPI 0.104+
 - **Database**: MySQL 8.0+
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **API Documentation**: Auto-generated with Swagger UI & ReDoc
- **Python**: 3.11+

## 📊 Database Architecture

### Core Modules

1. **Authentication & Users**
   - JWT-based authentication
   - OAuth support (Google, LinkedIn, GitHub)
   - Session management
   - User preferences

2. **User Profile**
   - Professional profiles with location
   - Skills with proficiency levels
   - Work experience history
   - Education background
   - Certifications & languages

3. **Jobs & Companies**
   - Company profiles with culture & values
   - Detailed job postings
   - Skills matching
   - Location-based search

4. **Tinder-Style Swiping**
   - Left swipe: Skip job
   - Right swipe: Interested (auto-apply optional)
   - Super swipe: Very interested
   - Swipe analytics & tracking

5. **Application System**
   - Application management
   - Status tracking (9 stages)
   - Interview scheduling
   - Offer management
   - Saved jobs with folders

6. **AI Features** (temporarily excluded)
   - To be enabled later (resumes, cover letters, recommendations, match score)

## 🗄️ Database Models

### User Management
- `users` - User accounts with OAuth
- `user_sessions` - Active JWT sessions
- `user_preferences` - Job search preferences

### Profile
- `profiles` - Professional information
- `skills` - User skills with proficiency
- `experiences` - Work history
- `educations` - Educational background
- `certifications` - Professional certs
- `languages` - Language proficiency

### Jobs
- `companies` - Company details
- `jobs` - Job postings
- `job_skills` - Required skills

### Applications
- `swipes` - Swipe history
- `applications` - Job applications
- `saved_jobs` - Bookmarked jobs

### AI & Matching
- `resumes` - AI-generated resumes
- `cover_letters` - AI cover letters
- `ai_recommendations` - AI suggestions
- `match_scores` - Detailed matching

## 🚀 Getting Started

### Prerequisites

```bash
# Required
- Python 3.11+
- MySQL 8.0+
- pip or poetry

# Optional
- Redis (for caching)
- AWS S3 (for file storage)
```

### Installation

1. **Navigate to backend directory**
   ```bash
   cd SwipeHire/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Create MySQL database**
   ```bash
   # Using MySQL CLI
   mysql -u root -p -e "CREATE DATABASE swipehire_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   ```

6. **Initialize database**
   ```bash
   # Create all tables
   python init_db.py
   
   # Drop and recreate (WARNING: deletes data)
   python init_db.py --drop
   ```

7. **Run the server**
   ```bash
   # Development mode (auto-reload)
   python main.py
   
   # Or with uvicorn directly
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   
   # Production mode
   uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

8. **Access API Documentation**
   ```
   Swagger UI: http://localhost:8000/docs
   ReDoc: http://localhost:8000/redoc
   ```

## 🔧 Configuration

### Environment Variables

Edit `.env` file (copy from `env.example`):

```env
# Database
DATABASE_URL="mysql+pymysql://root:password@localhost:3306/swipehire_dev"

# Security
SECRET_KEY="your-secret-key-here"

# AI Features
OPENAI_API_KEY="your-openai-key"

# File Storage (Optional)
AWS_ACCESS_KEY_ID="your-aws-key"
AWS_SECRET_ACCESS_KEY="your-aws-secret"
```

See `env.example` for all available options.

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── api/                    # API endpoints
│   │   └── v1/
│   ├── core/                   # Core functionality
│   │   ├── config.py          # Settings & config
│   │   └── database.py        # Database connection
│   ├── models/                 # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── base.py            # Base model class
│   │   ├── user.py            # User & auth models
│   │   ├── auth.py            # Session & preferences
│   │   ├── profile.py         # Profile models
│   │   ├── job.py             # Job & company models
│   │   ├── application.py     # Application & swipe
│   │   └── ai.py              # AI models
│   ├── schemas/                # Pydantic schemas
│   ├── services/               # Business logic
│   └── utils/                  # Utilities
├── alembic/                    # Database migrations
├── main.py                     # FastAPI app entry
├── init_db.py                  # DB initialization
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

## 🔑 Key Features for Flutter Frontend

### API Endpoints (Coming Soon)

- **Authentication**
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/login`
  - `POST /api/v1/auth/refresh`
  - `POST /api/v1/auth/logout`
  - OAuth: Google, LinkedIn

- **Profile Management**
  - `GET/PUT /api/v1/profile`
  - `POST /api/v1/skills`
  - `POST /api/v1/experience`
  - `POST /api/v1/education`

- **Job Swiping**
  - `GET /api/v1/jobs/feed` - Get swipeable jobs
  - `POST /api/v1/swipes` - Record swipe
  - `GET /api/v1/swipes/history`

- **Applications**
  - `POST /api/v1/applications` - Apply to job
  - `GET /api/v1/applications` - List applications
  - `PUT /api/v1/applications/{id}` - Update status

- **AI Features**
  - `POST /api/v1/resumes/generate` - AI resume
  - `POST /api/v1/cover-letters/generate` - AI cover letter
  - `GET /api/v1/recommendations` - Job recommendations
  - `GET /api/v1/match-score/{job_id}` - Match score

- **Search & Discovery**
  - `GET /api/v1/jobs/search`
  - `GET /api/v1/companies`
  - `POST /api/v1/saved-jobs`

## 🔒 Security Features

- **Password Security**: bcrypt hashing
- **JWT Authentication**: Access & refresh tokens
- **OAuth 2.0**: Google, LinkedIn, GitHub
- **Session Management**: Device tracking
- **Soft Deletes**: Data recovery
- **CORS**: Configured for Flutter apps

## 📊 Database Models Details

### Match Score Algorithm

9-factor weighted scoring:
- Skills Match: 30%
- Experience Level: 25%
- Education: 10%
- Location: 10%
- Salary Expectations: 10%
- Job Type: 5%
- Industry: 5%
- Company Culture: 3%
- Career Growth: 2%

### Swipe Analytics

Tracks:
- Time spent viewing
- Device type (mobile/tablet/desktop)
- Session context
- Auto-apply status
- Match score at swipe time

### Application Lifecycle

9 Status Stages:
1. Pending
2. Submitted
3. Under Review
4. Shortlisted
5. Interviewing
6. Offer Received
7. Accepted
8. Rejected
9. Withdrawn

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=app

# Watch mode
pytest-watch
```

## 🔄 Database Migrations (Alembic)

```bash
# Initialize Alembic (already done)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## 🚀 Deployment

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Using Gunicorn

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📱 Flutter Integration

### Example API Call from Flutter

```dart
// Login
final response = await http.post(
  Uri.parse('http://your-api.com/api/v1/auth/login'),
  headers: {'Content-Type': 'application/json'},
  body: jsonEncode({
    'email': 'user@example.com',
    'password': 'password123'
  }),
);

// Get job feed
final jobs = await http.get(
  Uri.parse('http://your-api.com/api/v1/jobs/feed'),
  headers: {'Authorization': 'Bearer $token'},
);

// Swipe right on job
await http.post(
  Uri.parse('http://your-api.com/api/v1/swipes'),
  headers: {
    'Authorization': 'Bearer $token',
    'Content-Type': 'application/json'
  },
  body: jsonEncode({
    'job_id': jobId,
    'direction': 'right',
    'auto_apply': true
  }),
);
```

## 📚 API Response Format

### Success Response
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message",
  "detail": "Detailed error description"
}
```

## 🤝 Contributing

1. Follow PEP 8 style guide
2. Write tests for new features
3. Update documentation
4. Use type hints
5. Format with Black

```bash
# Format code
black app/

# Lint
flake8 app/

# Type checking
mypy app/
```

## 📄 License

MIT License

## 👥 Team

SwipeHire Backend Team

## 📞 Support

- Documentation: `/docs` endpoint
- Issues: GitHub Issues
- Email: support@swipehire.com

---

Built with ❤️ using FastAPI & SQLAlchemy
