"""
Comprehensive seed database with 50+ artists
Combines initial 5 artists with extended timelines and 40+ additional artists
"""
from database import SessionLocal, engine, Base
from models import Artist, CareerEvent
from datetime import datetime

# Create tables
Base.metadata.create_all(bind=engine)

def seed_all_artists():
    db = SessionLocal()
    
    # Check if data already exists
    existing_artists = db.query(Artist).count()
    if existing_artists > 0:
        print(f"Database already has {existing_artists} artists. Skipping seed.")
        db.close()
        return
    
    print("🌱 Seeding database with 50+ artists...")
    
    # Import the original seed function for first 5 artists
    from seed_data import seed_database as seed_initial
    
    # Import the expansion function for 40+ more artists
    from expand_database import expand_database
    
    # Seed initial 5 artists
    print("  Adding initial 5 artists...")
    seed_initial()
    
    # Add 40+ more artists with extended timelines
    print("  Adding 40+ more artists...")
    expand_database()
    
    # Final count
    final_count = db.query(Artist).count()
    event_count = db.query(CareerEvent).count()
    
    print(f"\n✅ Database seeded successfully!")
    print(f"📊 Total Artists: {final_count}")
    print(f"📊 Total Career Events: {event_count}")
    
    db.close()

if __name__ == "__main__":
    seed_all_artists()
