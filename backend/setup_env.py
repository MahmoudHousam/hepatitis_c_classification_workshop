#!/usr/bin/env python3
"""
Environment setup helper for Hepatitis C Classification API
"""
import os
import sys

def create_env_file():
    """Create a .env file with template values"""
    env_content = """# Database Configuration
# Update this with your actual PostgreSQL credentials from Render
DATABASE_URL=postgresql://username:password@host.render.com:5432/database_name

# Model Configuration
MODEL_NAME=Hepatitis C Classification Model
MODEL_ACCURACY=0.85
MODEL_DATE_TRAINED=2024-01-15
MODEL_VERSION=1.0.0

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Example for Render PostgreSQL:
# DATABASE_URL=postgresql://username:password@host.render.com:5432/database_name
"""
    
    env_file_path = os.path.join(os.path.dirname(__file__), '.env')
    
    if os.path.exists(env_file_path):
        print(f"⚠️  .env file already exists at {env_file_path}")
        response = input("Do you want to overwrite it? (y/N): ").lower()
        if response != 'y':
            print("Setup cancelled.")
            return False
    
    try:
        with open(env_file_path, 'w') as f:
            f.write(env_content)
        print(f"✅ Created .env file at {env_file_path}")
        print("\n📝 Please update the DATABASE_URL with your actual PostgreSQL credentials from Render.")
        print("   The file contains template values that need to be customized.")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def print_setup_instructions():
    """Print setup instructions"""
    print("\n" + "="*60)
    print("SETUP INSTRUCTIONS")
    print("="*60)
    print("\n1. 📝 Update the .env file with your database credentials:")
    print("   - Get your PostgreSQL connection string from Render")
    print("   - Update the DATABASE_URL in the .env file")
    print("   - Format: postgresql://username:password@host:port/database")
    print("\n2. 🐍 Install Python dependencies:")
    print("   pip install -r requirements.txt")
    print("\n3. 🗄️  Initialize the database:")
    print("   python init_db.py")
    print("\n4. 🚀 Start the API server:")
    print("   python start.py")
    print("\n5. 🧪 Test the API:")
    print("   python test_api.py")
    print("\n6. 🌐 Access the API:")
    print("   - API: http://localhost:8000")
    print("   - Docs: http://localhost:8000/docs")
    print("   - Health: http://localhost:8000/health")

def main():
    """Main setup function"""
    print("🏥 Hepatitis C Classification API - Environment Setup")
    print("="*60)
    
    if create_env_file():
        print_setup_instructions()
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
