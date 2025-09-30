#!/usr/bin/env python3
"""
Database Initialization Script
Creates all database tables based on SQLAlchemy models
"""

import sys
from app.core.database import init_db, drop_db, engine
from app.models import *  # Import all models

def main():
    """Main function to initialize database"""
    
    if len(sys.argv) > 1 and sys.argv[1] == "--drop":
        print("⚠️  WARNING: This will drop all existing tables!")
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            drop_db()
        else:
            print("❌ Cancelled")
            return
    
    print("🔄 Initializing database...")
    init_db()
    print("✅ Database initialized successfully!")
    print("\n📊 Created tables:")
    
    from sqlalchemy import inspect
    inspector = inspect(engine)
    for table_name in inspector.get_table_names():
        print(f"  - {table_name}")

if __name__ == "__main__":
    main()
