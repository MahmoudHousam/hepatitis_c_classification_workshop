#!/usr/bin/env python3
"""
Database initialization script for Hepatitis C Classification API
"""
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import engine, SessionLocal
from models import Base, PredictionRecord
from config import settings

def init_database():
    """Initialize the database and create tables"""
    print("Initializing database...")
    print(f"Database URL: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'Not configured'}")
    
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        
        # Test database connection
        db = SessionLocal()
        try:
            # Try to query the database
            result = db.execute("SELECT 1")
            print("✅ Database connection successful!")
            
            # Check if tables exist
            tables = db.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """).fetchall()
            
            print(f"✅ Found {len(tables)} tables:")
            for table in tables:
                print(f"   - {table[0]}")
                
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
        finally:
            db.close()
            
        return True
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False

def test_sample_data():
    """Test inserting and querying sample data"""
    print("\nTesting sample data insertion...")
    
    try:
        db = SessionLocal()
        
        # Create a sample prediction record
        sample_record = PredictionRecord(
            age=35,
            sex="Female",
            alanine_aminotransferase=22.0,
            aspartate_aminotransferase=25.0,
            gamma_glutamyl_transferase=30.0,
            alkaline_phosphatase=80.0,
            total_bilirubin=0.7,
            direct_bilirubin=0.2,
            total_proteins=7.0,
            albumin=4.0,
            albumin_globulin_ratio=1.3,
            prediction="Negative",
            confidence=0.85
        )
        
        db.add(sample_record)
        db.commit()
        print("✅ Sample data inserted successfully!")
        
        # Query the data back
        records = db.query(PredictionRecord).all()
        print(f"✅ Found {len(records)} records in database")
        
        db.close()
        return True
        
    except Exception as e:
        print(f"❌ Sample data test failed: {e}")
        return False

def main():
    """Main initialization function"""
    print("=" * 60)
    print("Hepatitis C Classification - Database Initialization")
    print("=" * 60)
    
    # Initialize database
    if not init_database():
        print("\n❌ Database initialization failed. Please check your configuration.")
        sys.exit(1)
    
    # Test with sample data
    if test_sample_data():
        print("\n✅ Database initialization completed successfully!")
        print("\nYou can now start the API server with:")
        print("  python start.py")
        print("  or")
        print("  uvicorn main:app --host 0.0.0.0 --port 8000 --reload")
    else:
        print("\n❌ Sample data test failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
