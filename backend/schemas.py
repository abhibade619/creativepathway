from pydantic import BaseModel
from typing import List, Optional

# Artist Schemas
class CareerEventBase(BaseModel):
    age: int
    year: Optional[int] = None
    title: str
    description: Optional[str] = None
    event_type: Optional[str] = None
    risk_level: Optional[str] = None
    outcome: Optional[str] = None
    skills: Optional[List[str]] = []

class CareerEventCreate(CareerEventBase):
    artist_id: int

class CareerEvent(CareerEventBase):
    id: int
    artist_id: int
    
    class Config:
        from_attributes = True

class ArtistBase(BaseModel):
    name: str
    domain: str
    start_age: int
    first_break_age: Optional[int] = None
    training_type: Optional[str] = None
    constraints: Optional[str] = None
    starting_point: Optional[str] = None
    short_bio: Optional[str] = None
    image_url: Optional[str] = None

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int
    career_events: List[CareerEvent] = []
    
    class Config:
        from_attributes = True

# User Profile Schemas
class UserProfileBase(BaseModel):
    age: int
    domain: str
    experience_level: Optional[str] = "beginner"
    hours_per_week: Optional[int] = 10
    constraints: Optional[str] = None

class UserProfileCreate(UserProfileBase):
    pass

class UserProfile(UserProfileBase):
    id: int
    
    class Config:
        from_attributes = True

# Matching Schemas
class MatchRequest(BaseModel):
    user_profile: UserProfileCreate

class ArtistMatch(BaseModel):
    artist: Artist
    similarity_score: float
    match_reasons: List[str]
    events_at_user_age: List[CareerEvent]

class MatchResponse(BaseModel):
    matches: List[ArtistMatch]
    user_profile_id: int

# Roadmap Schemas
class RoadmapMonth(BaseModel):
    month: int
    title: str
    description: str
    inspired_by: Optional[str] = None  # Artist name
    decision_point: bool = False

class RoadmapRequest(BaseModel):
    user_profile_id: int
    selected_artist_ids: List[int]

class RoadmapResponse(BaseModel):
    roadmap_id: int
    months: List[RoadmapMonth]
