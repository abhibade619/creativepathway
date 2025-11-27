from typing import List
from sqlalchemy.orm import Session
from models import Artist as ArtistModel, CareerEvent as CareerEventModel, UserProfile as UserProfileModel
from schemas import RoadmapMonth

def generate_roadmap(
    user_profile: UserProfileModel,
    artists: List[ArtistModel],
    db: Session
) -> List[RoadmapMonth]:
    """
    Generate a 12-month personalized roadmap based on selected artists' early career events
    """
    roadmap = []
    
    # Collect early career events from all selected artists
    all_early_events = []
    for artist in artists:
        events = db.query(CareerEventModel).filter(
            CareerEventModel.artist_id == artist.id,
            CareerEventModel.age >= artist.start_age,
            CareerEventModel.age <= artist.start_age + 2  # First 2-3 years
        ).order_by(CareerEventModel.age).all()
        
        for event in events:
            all_early_events.append({
                'event': event,
                'artist': artist,
                'months_after_start': (event.age - artist.start_age) * 12
            })
    
    # Sort by timeline
    all_early_events.sort(key=lambda x: x['months_after_start'])
    
    # Create 12-month roadmap
    months_covered = set()
    
    # Month 1-3: Foundation
    roadmap.append(RoadmapMonth(
        month=1,
        title="Build Your Foundation",
        description="Start with the basics. Practice daily, even if just for 30 minutes. Study your craft and consume content from creators you admire.",
        inspired_by=artists[0].name if artists else None,
        decision_point=False
    ))
    
    roadmap.append(RoadmapMonth(
        month=2,
        title="Develop Your Skills",
        description="Focus on fundamental skills. Take online courses, watch tutorials, or find a mentor. Document your learning journey.",
        inspired_by=None,
        decision_point=False
    ))
    
    roadmap.append(RoadmapMonth(
        month=3,
        title="Create Your First Project",
        description="Start small. Create your first piece of work, even if it's not perfect. The goal is to complete something.",
        inspired_by=None,
        decision_point=True
    ))
    
    # Month 4-6: Early output
    event_idx = 0
    for month in range(4, 7):
        if event_idx < len(all_early_events):
            early_event = all_early_events[event_idx]
            roadmap.append(RoadmapMonth(
                month=month,
                title=f"Inspired by: {early_event['event'].title}",
                description=f"{early_event['artist'].name} did this at age {early_event['event'].age}: {early_event['event'].description or early_event['event'].title}. Consider doing something similar based on your resources.",
                inspired_by=early_event['artist'].name,
                decision_point=True
            ))
            event_idx += 1
        else:
            roadmap.append(RoadmapMonth(
                month=month,
                title="Continue Creating",
                description="Keep producing work consistently. Share your creations with friends or online communities for feedback.",
                inspired_by=None,
                decision_point=False
            ))
    
    # Month 7-9: Growth
    roadmap.append(RoadmapMonth(
        month=7,
        title="Expand Your Reach",
        description="Start building an online presence. Share your work on social media or relevant platforms. Engage with communities in your domain.",
        inspired_by=None,
        decision_point=False
    ))
    
    roadmap.append(RoadmapMonth(
        month=8,
        title="Collaborate",
        description="Find others in your field and collaborate. This could be a joint project, a feature, or simply learning together.",
        inspired_by=None,
        decision_point=True
    ))
    
    roadmap.append(RoadmapMonth(
        month=9,
        title="Refine Your Craft",
        description="Review your work from the past months. Identify areas for improvement and focus on leveling up specific skills.",
        inspired_by=None,
        decision_point=False
    ))
    
    # Month 10-12: Momentum
    roadmap.append(RoadmapMonth(
        month=10,
        title="Create Your Best Work Yet",
        description="Apply everything you've learned. Create something that showcases your growth and unique style.",
        inspired_by=None,
        decision_point=False
    ))
    
    roadmap.append(RoadmapMonth(
        month=11,
        title="Share and Promote",
        description="Release your best work. Promote it actively. Ask for feedback and engage with your growing audience.",
        inspired_by=None,
        decision_point=True
    ))
    
    roadmap.append(RoadmapMonth(
        month=12,
        title="Reflect and Plan Ahead",
        description="Look back at your year. Celebrate your progress. Set goals for the next 12 months based on what you've learned.",
        inspired_by=None,
        decision_point=False
    ))
    
    return roadmap
