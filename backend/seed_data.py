"""
Seed database with sample artist data
"""
from database import SessionLocal, engine, Base
from models import Artist, CareerEvent

# Create tables
Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    # Check if data already exists
    existing_artists = db.query(Artist).count()
    if existing_artists > 0:
        print(f"Database already has {existing_artists} artists. Skipping seed.")
        db.close()
        return
    
    # Artist 1: Taylor Swift
    taylor = Artist(
        name="Taylor Swift",
        domain="Singer-Songwriter",
        start_age=14,
        first_break_age=16,
        training_type="Formal (vocal lessons) + Self-taught (songwriting)",
        constraints="Moved to Nashville, family support",
        starting_point="Local performances, Nashville music scene",
        short_bio="Started writing songs at age 12, moved to Nashville at 14 to pursue country music career.",
        image_url="https://via.placeholder.com/300x300?text=Taylor+Swift"
    )
    db.add(taylor)
    db.flush()
    
    taylor_events = [
        CareerEvent(artist_id=taylor.id, age=12, year=2002, title="Started Writing Songs", 
                   description="Began writing her own songs and learning guitar", 
                   event_type="training", risk_level="low", outcome="positive", 
                   skills=["songwriting", "guitar"]),
        CareerEvent(artist_id=taylor.id, age=14, year=2004, title="Moved to Nashville", 
                   description="Family relocated to Nashville to support her music career", 
                   event_type="life_change", risk_level="high", outcome="positive", 
                   skills=["networking", "determination"]),
        CareerEvent(artist_id=taylor.id, age=14, year=2004, title="Performed at Bluebird Cafe", 
                   description="Regular performances at Nashville venues", 
                   event_type="performance", risk_level="medium", outcome="positive", 
                   skills=["live_performance", "confidence"]),
        CareerEvent(artist_id=taylor.id, age=15, year=2005, title="Signed with Big Machine Records", 
                   description="Became youngest artist signed by the label", 
                   event_type="milestone", risk_level="medium", outcome="positive", 
                   skills=["business", "negotiation"]),
        CareerEvent(artist_id=taylor.id, age=16, year=2006, title="Released Debut Single 'Tim McGraw'", 
                   description="First single reached Top 10 on country charts", 
                   event_type="release", risk_level="high", outcome="positive", 
                   skills=["recording", "marketing"]),
    ]
    db.add_all(taylor_events)
    
    # Artist 2: Ed Sheeran
    ed = Artist(
        name="Ed Sheeran",
        domain="Singer-Songwriter",
        start_age=11,
        first_break_age=20,
        training_type="Self-taught + School music programs",
        constraints="Small town, limited resources, worked odd jobs",
        starting_point="Local gigs, open mic nights, busking",
        short_bio="Started playing guitar at 11, moved to London at 16 to pursue music, played hundreds of small gigs.",
        image_url="https://via.placeholder.com/300x300?text=Ed+Sheeran"
    )
    db.add(ed)
    db.flush()
    
    ed_events = [
        CareerEvent(artist_id=ed.id, age=11, year=2002, title="Started Playing Guitar", 
                   description="Received first guitar and began learning", 
                   event_type="training", risk_level="low", outcome="positive", 
                   skills=["guitar", "music_theory"]),
        CareerEvent(artist_id=ed.id, age=13, year=2004, title="Wrote First Songs", 
                   description="Started writing original music", 
                   event_type="training", risk_level="low", outcome="positive", 
                   skills=["songwriting", "creativity"]),
        CareerEvent(artist_id=ed.id, age=14, year=2005, title="Recorded First EP", 
                   description="Self-produced and released first EP independently", 
                   event_type="release", risk_level="medium", outcome="positive", 
                   skills=["recording", "production", "self_promotion"]),
        CareerEvent(artist_id=ed.id, age=16, year=2007, title="Moved to London", 
                   description="Dropped out of school to pursue music full-time in London", 
                   event_type="life_change", risk_level="high", outcome="positive", 
                   skills=["risk_taking", "independence"]),
        CareerEvent(artist_id=ed.id, age=17, year=2008, title="Played 300+ Gigs", 
                   description="Performed at open mics, small venues, and busked on streets", 
                   event_type="performance", risk_level="medium", outcome="positive", 
                   skills=["live_performance", "persistence", "networking"]),
        CareerEvent(artist_id=ed.id, age=18, year=2009, title="Released Multiple EPs", 
                   description="Continued releasing independent music while building fanbase", 
                   event_type="release", risk_level="medium", outcome="positive", 
                   skills=["consistency", "branding"]),
    ]
    db.add_all(ed_events)
    
    # Artist 3: Billie Eilish
    billie = Artist(
        name="Billie Eilish",
        domain="Singer-Songwriter",
        start_age=13,
        first_break_age=14,
        training_type="Homeschooled, self-taught with brother",
        constraints="Worked from home studio, family collaboration",
        starting_point="SoundCloud, bedroom recordings",
        short_bio="Recorded 'Ocean Eyes' with her brother in their bedroom studio, uploaded to SoundCloud and went viral.",
        image_url="https://via.placeholder.com/300x300?text=Billie+Eilish"
    )
    db.add(billie)
    db.flush()
    
    billie_events = [
        CareerEvent(artist_id=billie.id, age=11, year=2013, title="Joined Los Angeles Children's Chorus", 
                   description="Began formal vocal training through choir", 
                   event_type="training", risk_level="low", outcome="positive", 
                   skills=["vocals", "harmony"]),
        CareerEvent(artist_id=billie.id, age=13, year=2015, title="Started Writing Songs with Brother", 
                   description="Collaborated with brother Finneas on original music", 
                   event_type="collaboration", risk_level="low", outcome="positive", 
                   skills=["songwriting", "collaboration"]),
        CareerEvent(artist_id=billie.id, age=14, year=2015, title="Recorded 'Ocean Eyes'", 
                   description="Recorded song in bedroom studio with brother", 
                   event_type="release", risk_level="medium", outcome="positive", 
                   skills=["recording", "production"]),
        CareerEvent(artist_id=billie.id, age=14, year=2016, title="'Ocean Eyes' Went Viral on SoundCloud", 
                   description="Song gained millions of streams organically", 
                   event_type="milestone", risk_level="low", outcome="positive", 
                   skills=["social_media", "authenticity"]),
        CareerEvent(artist_id=billie.id, age=15, year=2017, title="Signed with Interscope Records", 
                   description="Major label deal while maintaining creative control", 
                   event_type="milestone", risk_level="medium", outcome="positive", 
                   skills=["business", "negotiation"]),
    ]
    db.add_all(billie_events)
    
    # Artist 4: Chance the Rapper
    chance = Artist(
        name="Chance the Rapper",
        domain="Rapper",
        start_age=16,
        first_break_age=19,
        training_type="Self-taught, influenced by Chicago hip-hop scene",
        constraints="Stayed independent, no record label",
        starting_point="High school, local Chicago scene, free mixtapes",
        short_bio="Started rapping in high school, released free mixtapes independently, became first streaming-only artist to win Grammy.",
        image_url="https://via.placeholder.com/300x300?text=Chance+the+Rapper"
    )
    db.add(chance)
    db.flush()
    
    chance_events = [
        CareerEvent(artist_id=chance.id, age=16, year=2009, title="Started Rapping in High School", 
                   description="Began writing and performing rap music", 
                   event_type="training", risk_level="low", outcome="positive", 
                   skills=["rap", "writing", "rhythm"]),
        CareerEvent(artist_id=chance.id, age=18, year=2011, title="Suspended from School", 
                   description="10-day suspension led to recording first mixtape", 
                   event_type="life_change", risk_level="medium", outcome="positive", 
                   skills=["time_management", "focus"]),
        CareerEvent(artist_id=chance.id, age=19, year=2012, title="Released '10 Day' Mixtape", 
                   description="First mixtape released for free online, gained local attention", 
                   event_type="release", risk_level="medium", outcome="positive", 
                   skills=["production", "distribution", "marketing"]),
        CareerEvent(artist_id=chance.id, age=20, year=2013, title="Released 'Acid Rap' Mixtape", 
                   description="Second mixtape went viral, critical acclaim", 
                   event_type="release", risk_level="medium", outcome="positive", 
                   skills=["artistry", "innovation"]),
        CareerEvent(artist_id=chance.id, age=20, year=2013, title="Toured with Macklemore", 
                   description="First major tour as opening act", 
                   event_type="performance", risk_level="medium", outcome="positive", 
                   skills=["live_performance", "touring"]),
    ]
    db.add_all(chance_events)
    
    # Artist 5: Justin Bieber (YouTube Discovery)
    justin = Artist(
        name="Justin Bieber",
        domain="Singer",
        start_age=12,
        first_break_age=13,
        training_type="Self-taught (YouTube tutorials)",
        constraints="Small town Canada, single mother, limited resources",
        starting_point="YouTube covers, local talent competitions",
        short_bio="Posted singing covers on YouTube, discovered by talent manager Scooter Braun, became global phenomenon.",
        image_url="https://via.placeholder.com/300x300?text=Justin+Bieber"
    )
    db.add(justin)
    db.flush()
    
    justin_events = [
        CareerEvent(artist_id=justin.id, age=12, year=2006, title="Started Posting YouTube Videos", 
                   description="Mother posted videos of him singing covers", 
                   event_type="release", risk_level="low", outcome="positive", 
                   skills=["vocals", "social_media"]),
        CareerEvent(artist_id=justin.id, age=12, year=2006, title="Won Local Talent Competition", 
                   description="Placed second in local singing competition", 
                   event_type="performance", risk_level="low", outcome="positive", 
                   skills=["performance", "confidence"]),
        CareerEvent(artist_id=justin.id, age=13, year=2007, title="Discovered by Scooter Braun", 
                   description="Talent manager found him on YouTube", 
                   event_type="milestone", risk_level="low", outcome="positive", 
                   skills=["online_presence"]),
        CareerEvent(artist_id=justin.id, age=13, year=2008, title="Moved to Atlanta", 
                   description="Relocated to work with Usher and record music", 
                   event_type="life_change", risk_level="high", outcome="positive", 
                   skills=["adaptability", "professionalism"]),
        CareerEvent(artist_id=justin.id, age=14, year=2009, title="Signed with Island Records", 
                   description="Major label deal with RBMG/Island", 
                   event_type="milestone", risk_level="medium", outcome="positive", 
                   skills=["business"]),
        CareerEvent(artist_id=justin.id, age=15, year=2009, title="Released Debut Single 'One Time'", 
                   description="First single reached Top 20 in multiple countries", 
                   event_type="release", risk_level="high", outcome="positive", 
                   skills=["recording", "marketing"]),
    ]
    db.add_all(justin_events)
    
    db.commit()
    print("✅ Database seeded successfully with 5 artists and their career timelines!")
    db.close()

if __name__ == "__main__":
    seed_database()
