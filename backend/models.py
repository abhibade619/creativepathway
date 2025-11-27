from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class Artist(Base):
    __tablename__ = "artists"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    domain = Column(String, nullable=False)  # singer, rapper, producer, YouTuber, etc.
    start_age = Column(Integer, nullable=False)
    first_break_age = Column(Integer)
    training_type = Column(String)  # self-taught, formal, hybrid
    constraints = Column(String)  # small town, worked while practicing, etc.
    starting_point = Column(String)  # YouTube, local gigs, music school, etc.
    short_bio = Column(Text)
    image_url = Column(String)
    
    # Relationship
    career_events = relationship("CareerEvent", back_populates="artist", cascade="all, delete-orphan")

class CareerEvent(Base):
    __tablename__ = "career_events"
    
    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    age = Column(Integer, nullable=False)
    year = Column(Integer)
    title = Column(String, nullable=False)
    description = Column(Text)
    event_type = Column(String)  # release, performance, award, training, collaboration, etc.
    risk_level = Column(String)  # low, medium, high
    outcome = Column(String)  # positive, negative, neutral
    skills = Column(JSON)  # List of skills used/developed
    
    # Relationship
    artist = relationship("Artist", back_populates="career_events")

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    domain = Column(String, nullable=False)
    experience_level = Column(String)  # beginner, intermediate, advanced
    hours_per_week = Column(Integer)
    constraints = Column(String)  # working full-time, student, limited budget, etc.
    
class UserMatch(Base):
    __tablename__ = "user_matches"
    
    id = Column(Integer, primary_key=True, index=True)
    user_profile_id = Column(Integer, ForeignKey("user_profiles.id"))
    matched_artists = Column(JSON)  # List of artist IDs with similarity scores
    created_at = Column(String)

class UserRoadmap(Base):
    __tablename__ = "user_roadmaps"
    
    id = Column(Integer, primary_key=True, index=True)
    user_profile_id = Column(Integer, ForeignKey("user_profiles.id"))
    roadmap_data = Column(JSON)  # Month-by-month action plan
    created_at = Column(String)
