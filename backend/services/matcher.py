from typing import List
from sqlalchemy.orm import Session
from models import Artist as ArtistModel, CareerEvent as CareerEventModel, UserProfile as UserProfileModel
from schemas import ArtistMatch, Artist, CareerEvent

def calculate_similarity_score(user_profile: UserProfileModel, artist: ArtistModel) -> tuple[float, List[str]]:
    """
    Calculate similarity score between user and artist
    Returns: (score, reasons)
    """
    score = 0.0
    reasons = []
    
    # Age similarity (max 40 points)
    age_diff = abs(user_profile.age - artist.start_age)
    if age_diff == 0:
        score += 40
        reasons.append(f"Started at exactly the same age ({artist.start_age})")
    elif age_diff <= 2:
        score += 35
        reasons.append(f"Started at a very similar age ({artist.start_age})")
    elif age_diff <= 5:
        score += 25
        reasons.append(f"Started at age {artist.start_age}, close to your age")
    elif age_diff <= 10:
        score += 15
        reasons.append(f"Started at age {artist.start_age}")
    
    # Domain match (max 30 points)
    if user_profile.domain.lower() == artist.domain.lower():
        score += 30
        reasons.append(f"Same domain: {artist.domain}")
    elif user_profile.domain.lower() in artist.domain.lower() or artist.domain.lower() in user_profile.domain.lower():
        score += 20
        reasons.append(f"Related domain: {artist.domain}")
    
    # Training type match (max 15 points)
    if artist.training_type:
        if user_profile.experience_level == "beginner" and "self-taught" in artist.training_type.lower():
            score += 15
            reasons.append(f"Self-taught like you're planning")
        elif "formal" in artist.training_type.lower():
            score += 10
            reasons.append(f"Had formal training")
    
    # Time availability (max 15 points)
    if user_profile.hours_per_week:
        if user_profile.hours_per_week < 10 and artist.constraints and "worked" in artist.constraints.lower():
            score += 15
            reasons.append("Balanced creative work with other commitments")
        elif user_profile.hours_per_week >= 20:
            score += 10
            reasons.append("Dedicated significant time to their craft")
    
    return score, reasons

def find_matching_artists(
    user_profile: UserProfileModel, 
    artists: List[ArtistModel], 
    db: Session
) -> List[ArtistMatch]:
    """
    Find and rank artists similar to the user profile
    """
    matches = []
    
    for artist in artists:
        score, reasons = calculate_similarity_score(user_profile, artist)
        
        # Get events around user's age
        events_at_age = db.query(CareerEventModel).filter(
            CareerEventModel.artist_id == artist.id,
            CareerEventModel.age >= user_profile.age - 2,
            CareerEventModel.age <= user_profile.age + 2
        ).order_by(CareerEventModel.age).all()
        
        # Convert to schema
        artist_schema = Artist.from_orm(artist)
        events_schema = [CareerEvent.from_orm(event) for event in events_at_age]
        
        matches.append(ArtistMatch(
            artist=artist_schema,
            similarity_score=score,
            match_reasons=reasons,
            events_at_user_age=events_schema
        ))
    
    # Sort by similarity score (descending) and return top 5
    matches.sort(key=lambda x: x.similarity_score, reverse=True)
    return matches[:5]
