#!/usr/bin/env python3
"""
Quick Setup Script for SwipeHire Backend
Automates the setup process
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a shell command and print status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Done!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed!")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("🚀 SwipeHire Backend Setup")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("❌ Python 3.11+ required. Current version:", sys.version)
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")
    
    # Check if virtual environment exists
    venv_path = Path("venv")
    if not venv_path.exists():
        print("\n📦 Creating virtual environment...")
        if not run_command("python -m venv venv", "Create virtual environment"):
            sys.exit(1)
    else:
        print("\n✅ Virtual environment already exists")
    
    # Determine activation command based on OS
    if sys.platform == "win32":
        activate_cmd = r"venv\Scripts\activate"
        pip_cmd = r"venv\Scripts\pip"
        python_cmd = r"venv\Scripts\python"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
        python_cmd = "venv/bin/python"
    
    print(f"\n💡 To activate virtual environment, run:")
    print(f"   {activate_cmd}")
    
    # Install dependencies
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Install dependencies"):
        print("\n⚠️  Failed to install dependencies. Please run manually:")
        print(f"   {pip_cmd} install -r requirements.txt")
        sys.exit(1)
    
    # Check for .env file
    env_file = Path(".env")
    if not env_file.exists():
        env_example = Path("env.example")
        if env_example.exists():
            print("\n📝 Creating .env file from template...")
            with open(env_example, 'r') as src, open(env_file, 'w') as dst:
                dst.write(src.read())
            print("✅ .env file created!")
            print("⚠️  Please edit .env with your configuration:")
            print("   - DATABASE_URL")
            print("   - SECRET_KEY")
            print("   - OPENAI_API_KEY (for AI features)")
        else:
            print("\n❌ env.example not found!")
    else:
        print("\n✅ .env file already exists")
    
    # Database setup
    print("\n" + "=" * 60)
    print("📊 Database Setup")
    print("=" * 60)
    print("\nPlease ensure PostgreSQL is running and database is created:")
    print("   createdb swipehire_dev")
    print("\nOr with SQL:")
    print("   psql -U postgres")
    print("   CREATE DATABASE swipehire_dev;")
    
    init_db = input("\n🔧 Initialize database tables? (yes/no): ").lower()
    if init_db == "yes":
        if not run_command(f"{python_cmd} init_db.py", "Initialize database"):
            print("\n⚠️  Database initialization failed. Please check:")
            print("   - PostgreSQL is running")
            print("   - Database exists")
            print("   - DATABASE_URL in .env is correct")
    
    # Success message
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    print("\n🚀 To start the server:")
    print(f"   {activate_cmd}")
    print(f"   {python_cmd} main.py")
    print("\n📚 API Documentation will be available at:")
    print("   http://localhost:8000/docs")
    print("\n💡 Next steps:")
    print("   1. Edit .env with your configuration")
    print("   2. Ensure PostgreSQL database is created")
    print("   3. Run: python init_db.py (if not done)")
    print("   4. Start server: python main.py")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
