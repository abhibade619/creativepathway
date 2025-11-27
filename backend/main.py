from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import artists, matching, roadmap

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Creative Pathways Explorer API",
    description="API for matching aspiring creators with successful artist career paths",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],  # Vite dev server
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
