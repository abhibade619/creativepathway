from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from models import Artist as ArtistModel, CareerEvent as CareerEventModel
from schemas import Artist, ArtistCreate, CareerEvent

router = APIRouter()

@router.get("/", response_model=List[Artist])
def get_artists(
    domain: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all artists with optional filtering by domain (partial match)"""
    query = db.query(ArtistModel)
    
    if domain:
        # Use partial matching - case insensitive
        query = query.filter(ArtistModel.domain.ilike(f"%{domain}%"))
    
    artists = query.offset(skip).limit(limit).all()
    return artists

@router.get("/{artist_id}", response_model=Artist)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    """Get a specific artist by ID"""
    artist = db.query(ArtistModel).filter(ArtistModel.id == artist_id).first()
    
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    return artist

@router.get("/{artist_id}/timeline", response_model=List[CareerEvent])
def get_artist_timeline(artist_id: int, db: Session = Depends(get_db)):
    """Get career timeline for a specific artist"""
    artist = db.query(ArtistModel).filter(ArtistModel.id == artist_id).first()
    
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    # Return events sorted by age
    events = db.query(CareerEventModel).filter(
        CareerEventModel.artist_id == artist_id
    ).order_by(CareerEventModel.age).all()
    
    return events

@router.post("/", response_model=Artist)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    """Create a new artist (admin function)"""
    db_artist = ArtistModel(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist
