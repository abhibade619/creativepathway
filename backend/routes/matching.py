from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Artist as ArtistModel, CareerEvent as CareerEventModel, UserProfile as UserProfileModel
from schemas import MatchRequest, MatchResponse, ArtistMatch
from services.matcher import find_matching_artists

router = APIRouter()

@router.post("/", response_model=MatchResponse)
def match_user_with_artists(request: MatchRequest, db: Session = Depends(get_db)):
    """
    Match user profile with similar artists based on:
    - Age similarity
    - Domain match
    - Training type
    - Constraints
    """
    # Save user profile
    user_profile = UserProfileModel(**request.user_profile.dict())
    db.add(user_profile)
    db.commit()
    db.refresh(user_profile)
    
    # Get all artists
    artists = db.query(ArtistModel).all()
    
    # Find matches
    matches = find_matching_artists(user_profile, artists, db)
    
    return MatchResponse(
        matches=matches,
        user_profile_id=user_profile.id
    )
