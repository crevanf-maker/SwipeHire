from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the centralized settings object
from app.core.config import settings

# Import the core components we have been using
from database import engine, Base
from models import *  # This will find and register all your models (User, Profile, etc.)
from routers import auth, profiles  # Import both of our feature routers
from routers import auth, profiles, skills

# This crucial line tells SQLAlchemy to create all the tables
# defined in models.py when the app starts.
Base.metadata.create_all(bind=engine)

# Create the main FastAPI application instance using settings from your config file
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered job application platform with Tinder-like swiping interface",
)

# Configure CORS using settings from your config file
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Lifespan Events (for startup and shutdown) ---
@app.on_event("startup")
def startup_event():
    """Prints a nice message when the application starts."""
    print(f"🚀 Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"📝 API Documentation available at: /docs")


@app.on_event("shutdown")
def shutdown_event():
    """Prints a nice message when the application shuts down."""
    print(f"👋 Shutting down {settings.APP_NAME}")


# --- Include Routers ---
# This makes the endpoints from your router files available in the main app.
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(profiles.router, prefix="/api/profiles", tags=["Profiles"])
app.include_router(skills.router, prefix="/api/skills", tags=["Skills"])


# --- Root and Health Check Endpoints ---
@app.get("/")
def root():
    """A simple root endpoint to confirm the API is running."""
    return {"status": "ok", "message": f"Welcome to {settings.APP_NAME}"}


@app.get("/health")
def health_check():
    """A health check endpoint that can be used by monitoring services."""
    return {"status": "healthy"}
