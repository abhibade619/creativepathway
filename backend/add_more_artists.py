"""
Add more artists with extended timelines to current age
Run this after the initial seed_data.py
"""
from database import SessionLocal, engine, Base
from models import Artist, CareerEvent
from datetime import datetime

def add_more_artists():
    db = SessionLocal()
    
    # Get current count
    existing_count = db.query(Artist).count()
    print(f"Current artists in database: {existing_count}")
    
    # Artist 6: MrBeast (YouTuber)
    mrbeast = Artist(
        name="MrBeast (Jimmy Donaldson)",
        domain="YouTuber/Content Creator",
        start_age=13,
        first_break_age=18,
        training_type="Self-taught, trial and error",
        constraints="Started with minimal budget, worked while creating",
        starting_point="YouTube gaming videos",
        short_bio="Started making YouTube videos at 13, became one of the biggest YouTubers through viral challenges and philanthropy.",
        image_url="https://via.placeholder.com/300x300?text=MrBeast"
    )
    db.add(mrbeast)
    db.flush()
    
    current_year = datetime.now().year
    mrbeast_events = [
        CareerEvent(artist_id=mrbeast.id, age=13, year=2011, title="Started YouTube Channel",
                   description="Created first YouTube channel posting gaming videos and commentary",
                   event_type="training", risk_level="low", outcome="positive",
                   skills=["video_editing", "content_creation"]),
        CareerEvent(artist_id=mrbeast.id, age=15, year=2013, title="Studied Viral Content",
                   description="Analyzed thousands of viral videos to understand what works",
                   event_type="training", risk_level="low", outcome="positive",
                   skills=["analytics", "pattern_recognition"]),
        CareerEvent(artist_id=mrbeast.id, age=18, year=2016, title="'Counting to 100,000' Video",
                   description="Viral video that took 40 hours to film, gained millions of views",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["persistence", "viral_content"]),
        CareerEvent(artist_id=mrbeast.id, age=19, year=2017, title="Dropped Out of College",
                   description="Left college to focus full-time on YouTube",
                   event_type="life_change", risk_level="high", outcome="positive",
                   skills=["risk_taking", "commitment"]),
        CareerEvent(artist_id=mrbeast.id, age=20, year=2018, title="Started Large-Scale Challenges",
                   description="Began creating expensive challenge videos with big prizes",
                   event_type="milestone", risk_level="high", outcome="positive",
                   skills=["production", "fundraising"]),
        CareerEvent(artist_id=mrbeast.id, age=22, year=2020, title="Launched MrBeast Burger",
                   description="Started virtual restaurant brand with 300+ locations",
                   event_type="milestone", risk_level="high", outcome="positive",
                   skills=["business", "branding"]),
        CareerEvent(artist_id=mrbeast.id, age=24, year=2022, title="100M Subscribers",
                   description="Reached 100 million YouTube subscribers",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["audience_building", "consistency"]),
        CareerEvent(artist_id=mrbeast.id, age=26, year=2024, title="Largest YouTuber",
                   description="Became most-subscribed individual YouTuber with 200M+ subscribers",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["innovation", "scale"]),
    ]
    db.add_all(mrbeast_events)
    
    # Artist 7: Lilly Singh (YouTuber to TV Host)
    lilly = Artist(
        name="Lilly Singh",
        domain="YouTuber/Comedian/TV Host",
        start_age=21,
        first_break_age=23,
        training_type="Self-taught comedy, psychology degree",
        constraints="Dealt with depression, started while in university",
        starting_point="YouTube comedy sketches",
        short_bio="Started YouTube channel 'Superwoman' while dealing with depression, became late-night TV host.",
        image_url="https://via.placeholder.com/300x300?text=Lilly+Singh"
    )
    db.add(lilly)
    db.flush()
    
    lilly_events = [
        CareerEvent(artist_id=lilly.id, age=21, year=2010, title="Started YouTube Channel",
                   description="Created 'IISuperwomanII' channel posting comedy sketches",
                   event_type="training", risk_level="medium", outcome="positive",
                   skills=["comedy", "video_production"]),
        CareerEvent(artist_id=lilly.id, age=23, year=2012, title="Viral 'Types of People' Series",
                   description="Comedy series went viral, gained millions of subscribers",
                   event_type="release", risk_level="medium", outcome="positive",
                   skills=["character_acting", "writing"]),
        CareerEvent(artist_id=lilly.id, age=25, year=2014, title="First World Tour",
                   description="'A Trip to Unicorn Island' tour across multiple countries",
                   event_type="performance", risk_level="high", outcome="positive",
                   skills=["live_performance", "touring"]),
        CareerEvent(artist_id=lilly.id, age=27, year=2016, title="Released Book 'How to Be a Bawse'",
                   description="New York Times bestseller",
                   event_type="release", risk_level="medium", outcome="positive",
                   skills=["writing", "publishing"]),
        CareerEvent(artist_id=lilly.id, age=30, year=2019, title="NBC Late Night Show Host",
                   description="Became first woman of color to host late-night talk show",
                   event_type="milestone", risk_level="high", outcome="positive",
                   skills=["hosting", "interviewing"]),
        CareerEvent(artist_id=lilly.id, age=35, year=2024, title="Multi-Platform Creator",
                   description="Continues creating across YouTube, TV, and social media",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["adaptation", "multi_platform"]),
    ]
    db.add_all(lilly_events)
    
    # Artist 8: Zedd (DJ/Producer)
    zedd = Artist(
        name="Zedd (Anton Zaslavski)",
        domain="DJ/Music Producer",
        start_age=12,
        first_break_age=22,
        training_type="Classical music training, self-taught production",
        constraints="Immigrant family, limited resources",
        starting_point="Classical piano, electronic music production",
        short_bio="Classically trained musician who transitioned to electronic music production and became a top DJ.",
        image_url="https://via.placeholder.com/300x300?text=Zedd"
    )
    db.add(zedd)
    db.flush()
    
    zedd_events = [
        CareerEvent(artist_id=zedd.id, age=12, year=2002, title="Started Classical Piano",
                   description="Began formal classical music training",
                   event_type="training", risk_level="low", outcome="positive",
                   skills=["piano", "music_theory"]),
        CareerEvent(artist_id=zedd.id, age=16, year=2006, title="Discovered Electronic Music",
                   description="Started experimenting with electronic music production",
                   event_type="training", risk_level="low", outcome="positive",
                   skills=["production", "synthesis"]),
        CareerEvent(artist_id=zedd.id, age=20, year=2010, title="Released First Tracks",
                   description="Started releasing music on Beatport and SoundCloud",
                   event_type="release", risk_level="medium", outcome="positive",
                   skills=["distribution", "marketing"]),
        CareerEvent(artist_id=zedd.id, age=22, year=2012, title="'Clarity' Released",
                   description="Breakthrough single featuring Foxes, went multi-platinum",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["songwriting", "collaboration"]),
        CareerEvent(artist_id=zedd.id, age=23, year=2013, title="Won Grammy Award",
                   description="Grammy for Best Dance Recording for 'Clarity'",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["recognition", "achievement"]),
        CareerEvent(artist_id=zedd.id, age=25, year=2015, title="'I Want You To Know' with Selena Gomez",
                   description="Collaboration with major pop artist, mainstream success",
                   event_type="collaboration", risk_level="medium", outcome="positive",
                   skills=["networking", "crossover"]),
        CareerEvent(artist_id=zedd.id, age=28, year=2018, title="'The Middle' with Maren Morris",
                   description="Massive hit, Billboard Hot 100 top 5",
                   event_type="release", risk_level="medium", outcome="positive",
                   skills=["hit_making", "production"]),
        CareerEvent(artist_id=zedd.id, age=34, year=2024, title="Headlining Major Festivals",
                   description="Regular headliner at Coachella, EDC, Tomorrowland",
                   event_type="performance", risk_level="low", outcome="positive",
                   skills=["live_performance", "stage_production"]),
    ]
    db.add_all(zedd_events)
    
    # Artist 9: Emma Chamberlain (YouTuber/Entrepreneur)
    emma = Artist(
        name="Emma Chamberlain",
        domain="YouTuber/Entrepreneur",
        start_age=16,
        first_break_age=17,
        training_type="Self-taught video editing and content creation",
        constraints="High school student, anxiety and depression",
        starting_point="YouTube vlogs",
        short_bio="Started vlogging in high school, became one of the most influential Gen Z creators and entrepreneurs.",
        image_url="https://via.placeholder.com/300x300?text=Emma+Chamberlain"
    )
    db.add(emma)
    db.flush()
    
    emma_events = [
        CareerEvent(artist_id=emma.id, age=16, year=2017, title="Started YouTube Channel",
                   description="Posted first vlogs while in high school",
                   event_type="training", risk_level="low", outcome="positive",
                   skills=["vlogging", "editing"]),
        CareerEvent(artist_id=emma.id, age=17, year=2018, title="Viral Editing Style",
                   description="Unique fast-paced editing style went viral, gained millions of subscribers",
                   event_type="milestone", risk_level="medium", outcome="positive",
                   skills=["editing", "authenticity"]),
        CareerEvent(artist_id=emma.id, age=17, year=2018, title="Dropped Out of High School",
                   description="Left high school to pursue YouTube full-time",
                   event_type="life_change", risk_level="high", outcome="positive",
                   skills=["risk_taking", "commitment"]),
        CareerEvent(artist_id=emma.id, age=18, year=2019, title="Met Gala Attendance",
                   description="Invited to Met Gala, became fashion icon",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["fashion", "branding"]),
        CareerEvent(artist_id=emma.id, age=19, year=2020, title="Launched Chamberlain Coffee",
                   description="Started own coffee company",
                   event_type="milestone", risk_level="high", outcome="positive",
                   skills=["entrepreneurship", "business"]),
        CareerEvent(artist_id=emma.id, age=21, year=2022, title="Podcast 'Anything Goes'",
                   description="Launched successful podcast reaching #1 on charts",
                   event_type="release", risk_level="medium", outcome="positive",
                   skills=["podcasting", "storytelling"]),
        CareerEvent(artist_id=emma.id, age=23, year=2024, title="Multi-Platform Influencer",
                   description="12M+ YouTube subscribers, successful business owner",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["influence", "diversification"]),
    ]
    db.add_all(emma_events)
    
    # Artist 10: Donald Glover (Childish Gambino - Multi-hyphenate)
    donald = Artist(
        name="Donald Glover (Childish Gambino)",
        domain="Rapper/Actor/Writer/Director",
        start_age=23,
        first_break_age=26,
        training_type="NYU Tisch School of the Arts",
        constraints="Worked multiple jobs while pursuing entertainment",
        starting_point="Comedy writing, stand-up",
        short_bio="Multi-talented creator who succeeded as writer, actor, comedian, rapper, and director.",
        image_url="https://via.placeholder.com/300x300?text=Donald+Glover"
    )
    db.add(donald)
    db.flush()
    
    donald_events = [
        CareerEvent(artist_id=donald.id, age=23, year=2006, title="Hired as Writer for '30 Rock'",
                   description="Became writer for NBC's 30 Rock at age 23",
                   event_type="milestone", risk_level="medium", outcome="positive",
                   skills=["writing", "comedy"]),
        CareerEvent(artist_id=donald.id, age=26, year=2009, title="Cast in 'Community'",
                   description="Breakthrough acting role as Troy Barnes",
                   event_type="milestone", risk_level="medium", outcome="positive",
                   skills=["acting", "improvisation"]),
        CareerEvent(artist_id=donald.id, age=28, year=2011, title="Released First Mixtape as Childish Gambino",
                   description="Started music career under stage name Childish Gambino",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["rapping", "music_production"]),
        CareerEvent(artist_id=donald.id, age=30, year=2013, title="Album 'Because the Internet'",
                   description="Critically acclaimed album with accompanying screenplay",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["concept_creation", "multimedia"]),
        CareerEvent(artist_id=donald.id, age=33, year=2016, title="Created 'Atlanta' TV Series",
                   description="Created, wrote, directed, and starred in FX's Atlanta",
                   event_type="milestone", risk_level="high", outcome="positive",
                   skills=["directing", "showrunning"]),
        CareerEvent(artist_id=donald.id, age=34, year=2017, title="Won Emmy Awards",
                   description="Won Emmy for directing and acting in Atlanta",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["recognition", "excellence"]),
        CareerEvent(artist_id=donald.id, age=35, year=2018, title="'This Is America' Released",
                   description="Viral music video addressing social issues, won Grammy",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["social_commentary", "viral_content"]),
        CareerEvent(artist_id=donald.id, age=40, year=2023, title="Multi-Platform Success",
                   description="Continued success across music, TV, film (Star Wars, Lion King)",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["versatility", "sustained_success"]),
    ]
    db.add_all(donald_events)
    
    # Artist 11: Dua Lipa (Singer)
    dua = Artist(
        name="Dua Lipa",
        domain="Singer/Songwriter",
        start_age=14,
        first_break_age=20,
        training_type="Self-taught, YouTube covers",
        constraints="Immigrant family, worked as model while pursuing music",
        starting_point="YouTube covers, modeling",
        short_bio="Posted YouTube covers as a teen, worked as model, became global pop star.",
        image_url="https://via.placeholder.com/300x300?text=Dua+Lipa"
    )
    db.add(dua)
    db.flush()
    
    dua_events = [
        CareerEvent(artist_id=dua.id, age=14, year=2009, title="Started Posting YouTube Covers",
                   description="Began posting covers of favorite songs on YouTube",
                   event_type="training", risk_level="low", outcome="positive",
                   skills=["vocals", "performance"]),
        CareerEvent(artist_id=dua.id, age=16, year=2011, title="Moved to London",
                   description="Moved to London to pursue music career",
                   event_type="life_change", risk_level="high", outcome="positive",
                   skills=["independence", "determination"]),
        CareerEvent(artist_id=dua.id, age=17, year=2012, title="Worked as Model",
                   description="Modeled to support herself while pursuing music",
                   event_type="training", risk_level="medium", outcome="positive",
                   skills=["work_ethic", "networking"]),
        CareerEvent(artist_id=dua.id, age=20, year=2015, title="Signed Record Deal",
                   description="Signed with Warner Bros Records",
                   event_type="milestone", risk_level="medium", outcome="positive",
                   skills=["business", "negotiation"]),
        CareerEvent(artist_id=dua.id, age=21, year=2016, title="Released 'Be the One'",
                   description="First major single, charted in multiple countries",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["songwriting", "recording"]),
        CareerEvent(artist_id=dua.id, age=22, year=2017, title="Debut Album Released",
                   description="Self-titled debut album, went platinum",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["album_creation", "artistry"]),
        CareerEvent(artist_id=dua.id, age=23, year=2018, title="'New Rules' Global Hit",
                   description="Breakthrough hit reached #1 in multiple countries",
                   event_type="release", risk_level="medium", outcome="positive",
                   skills=["hit_making", "global_appeal"]),
        CareerEvent(artist_id=dua.id, age=24, year=2019, title="Won Grammy Awards",
                   description="Won Best New Artist and Best Dance Recording",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["recognition", "achievement"]),
        CareerEvent(artist_id=dua.id, age=25, year=2020, title="'Future Nostalgia' Album",
                   description="Critically acclaimed second album during pandemic",
                   event_type="release", risk_level="high", outcome="positive",
                   skills=["innovation", "timing"]),
        CareerEvent(artist_id=dua.id, age=28, year=2023, title="Global Superstar",
                   description="World tours, brand partnerships, continued chart success",
                   event_type="milestone", risk_level="low", outcome="positive",
                   skills=["touring", "brand_building"]),
    ]
    db.add_all(dua_events)
    
    db.commit()
    print(f"\n✅ Successfully added 6 more artists!")
    print(f"Total artists in database: {db.query(Artist).count()}")
    print(f"Total career events: {db.query(CareerEvent).count()}")
    
    print("\nNew artists added:")
    print("- MrBeast (YouTuber/Content Creator)")
    print("- Lilly Singh (YouTuber/Comedian/TV Host)")
    print("- Zedd (DJ/Music Producer)")
    print("- Emma Chamberlain (YouTuber/Entrepreneur)")
    print("- Donald Glover/Childish Gambino (Multi-hyphenate)")
    print("- Dua Lipa (Singer/Songwriter)")
    
    db.close()

if __name__ == "__main__":
    add_more_artists()
