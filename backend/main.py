from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, SessionLocal
from routes import artists, matching, roadmap
from models import Artist
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Creative Pathways Explorer API",
    description="API for matching aspiring creators with successful artist career paths",
    version="1.0.0"
)

# Startup event to seed database if empty
@app.on_event("startup")
async def startup_event():
    """Initialize database with seed data if empty"""
    db = SessionLocal()
    try:
        artist_count = db.query(Artist).count()
        if artist_count == 0:
            print("🌱 Database is empty, seeding with all artists...")
            # Import comprehensive seed function
            from seed_all import seed_all_artists
            seed_all_artists()
            print("✅ Database seeded with 50+ artists!")
        else:
            print(f"✅ Database already has {artist_count} artists")
    except Exception as e:
        print(f"⚠️ Error during database initialization: {e}")
        # Fallback to basic seed if comprehensive seed fails
        try:
            from seed_data import seed_database
            seed_database()
        except:
            pass
    finally:
        db.close()

# Configure CORS - allow production domain
allowed_origins = [
    "http://localhost:5173",
    "http://localhost:5174",
]

# Add production domain from environment variable if available
cors_origins_env = os.getenv("BACKEND_CORS_ORIGINS")
if cors_origins_env:
    import json
    try:
        prod_origins = json.loads(cors_origins_env)
        allowed_origins.extend(prod_origins)
    except:
        pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(artists.router, prefix="/api/artists", tags=["Artists"])
app.include_router(matching.router, prefix="/api/match", tags=["Matching"])
app.include_router(roadmap.router, prefix="/api/roadmap", tags=["Roadmap"])

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Creative Pathways Explorer API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
