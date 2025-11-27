"""
Initialize database on startup if empty
"""
from database import SessionLocal, engine, Base
from models import Artist
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def init_db():
    """Initialize database tables and seed if empty"""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Check if database is empty
    db = SessionLocal()
    artist_count = db.query(Artist).count()
    
    if artist_count == 0:
        print("Database is empty, seeding with initial data...")
        db.close()
        
        # Import and run seed script
        from seed_data import seed_database
        seed_database()
        
        print("Database seeded successfully!")
    else:
        print(f"Database already has {artist_count} artists")
        db.close()

if __name__ == "__main__":
    init_db()
