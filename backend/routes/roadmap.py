from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import UserProfile as UserProfileModel, Artist as ArtistModel, UserRoadmap as UserRoadmapModel
from schemas import RoadmapRequest, RoadmapResponse
from services.roadmap_generator import generate_roadmap
from datetime import datetime

router = APIRouter()

@router.post("/generate", response_model=RoadmapResponse)
def create_roadmap(request: RoadmapRequest, db: Session = Depends(get_db)):
    """
    Generate a personalized 12-month roadmap based on selected artists
    """
    # Get user profile
    user_profile = db.query(UserProfileModel).filter(
        UserProfileModel.id == request.user_profile_id
    ).first()
    
    if not user_profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    
    # Get selected artists
    artists = db.query(ArtistModel).filter(
        ArtistModel.id.in_(request.selected_artist_ids)
    ).all()
    
    if not artists:
        raise HTTPException(status_code=404, detail="No artists found")
    
    # Generate roadmap
    roadmap_months = generate_roadmap(user_profile, artists, db)
    
    # Save roadmap
    roadmap = UserRoadmapModel(
        user_profile_id=user_profile.id,
        roadmap_data=[month.dict() for month in roadmap_months],
        created_at=datetime.now().isoformat()
    )
    db.add(roadmap)
    db.commit()
    db.refresh(roadmap)
    
    return RoadmapResponse(
        roadmap_id=roadmap.id,
        months=roadmap_months
    )

@router.get("/{roadmap_id}")
def get_roadmap(roadmap_id: int, db: Session = Depends(get_db)):
    """Retrieve a saved roadmap"""
    roadmap = db.query(UserRoadmapModel).filter(
        UserRoadmapModel.id == roadmap_id
    ).first()
    
    if not roadmap:
        raise HTTPException(status_code=404, detail="Roadmap not found")
    
    return roadmap
