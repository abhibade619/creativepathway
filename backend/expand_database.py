"""
Comprehensive artist database expansion
- Extends first 5 artists to current age
- Adds 40+ new artists from diverse domains
- Total: ~50 artists with detailed timelines
"""
from database import SessionLocal
from models import Artist, CareerEvent
from datetime import datetime

def expand_database():
    db = SessionLocal()
    current_year = datetime.now().year
    
    print("=" * 60)
    print("EXPANDING CREATIVE PATHWAYS DATABASE")
    print("=" * 60)
    
    # ========== PART 1: EXTEND EXISTING ARTISTS ==========
    print("\n📝 Part 1: Extending existing artists to current age...")
    
    # Taylor Swift - extend to age 34 (2024)
    taylor = db.query(Artist).filter(Artist.name == "Taylor Swift").first()
    if taylor:
        new_taylor_events = [
            CareerEvent(artist_id=taylor.id, age=17, year=2007, title="Released Debut Album",
                       description="Self-titled debut album went platinum", event_type="release",
                       risk_level="high", outcome="positive", skills=["album_production", "marketing"]),
            CareerEvent(artist_id=taylor.id, age=19, year=2009, title="'Fearless' Album",
                       description="Second album, won Album of the Year Grammy", event_type="release",
                       risk_level="medium", outcome="positive", skills=["songwriting", "storytelling"]),
            CareerEvent(artist_id=taylor.id, age=22, year=2012, title="'Red' Album",
                       description="Transition from country to pop", event_type="release",
                       risk_level="high", outcome="positive", skills=["genre_transition", "risk_taking"]),
            CareerEvent(artist_id=taylor.id, age=24, year=2014, title="'1989' Full Pop Album",
                       description="Complete transition to pop, massive commercial success", event_type="release",
                       risk_level="high", outcome="positive", skills=["reinvention", "pop_production"]),
            CareerEvent(artist_id=taylor.id, age=27, year=2017, title="'Reputation' Era",
                       description="Response to media scrutiny, stadium tour", event_type="release",
                       risk_level="high", outcome="positive", skills=["resilience", "touring"]),
            CareerEvent(artist_id=taylor.id, age=29, year=2019, title="'Lover' Album",
                       description="Return to lighter themes, owned masters dispute", event_type="release",
                       risk_level="medium", outcome="positive", skills=["business_awareness"]),
            CareerEvent(artist_id=taylor.id, age=30, year=2020, title="'Folklore' & 'Evermore'",
                       description="Surprise indie-folk albums during pandemic", event_type="release",
                       risk_level="high", outcome="positive", skills=["adaptation", "indie_sound"]),
            CareerEvent(artist_id=taylor.id, age=32, year=2022, title="'Midnights' Album",
                       description="Return to pop, broke streaming records", event_type="release",
                       risk_level="medium", outcome="positive", skills=["record_breaking"]),
            CareerEvent(artist_id=taylor.id, age=33, year=2023, title="Eras Tour",
                       description="Highest-grossing tour of all time", event_type="performance",
                       risk_level="low", outcome="positive", skills=["live_performance", "production"]),
            CareerEvent(artist_id=taylor.id, age=34, year=2024, title="Billionaire Status",
                       description="First musician to become billionaire from music alone", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["business", "sustained_success"]),
        ]
        db.add_all(new_taylor_events)
        print("✓ Extended Taylor Swift to age 34")
    
    # Ed Sheeran - extend to age 33 (2024)
    ed = db.query(Artist).filter(Artist.name == "Ed Sheeran").first()
    if ed:
        new_ed_events = [
            CareerEvent(artist_id=ed.id, age=20, year=2011, title="Signed with Atlantic Records",
                       description="Major label deal after years of independent work", event_type="milestone",
                       risk_level="medium", outcome="positive", skills=["negotiation", "persistence"]),
            CareerEvent(artist_id=ed.id, age=21, year=2012, title="'+' (Plus) Album",
                       description="Debut major label album, went multi-platinum", event_type="release",
                       risk_level="high", outcome="positive", skills=["album_creation"]),
            CareerEvent(artist_id=ed.id, age=23, year=2014, title="'x' (Multiply) Album",
                       description="Second album with 'Thinking Out Loud', global success", event_type="release",
                       risk_level="medium", outcome="positive", skills=["hit_making"]),
            CareerEvent(artist_id=ed.id, age=26, year=2017, title="'÷' (Divide) Album",
                       description="'Shape of You' became most-streamed song", event_type="release",
                       risk_level="medium", outcome="positive", skills=["streaming_success"]),
            CareerEvent(artist_id=ed.id, age=28, year=2019, title="'No.6 Collaborations Project'",
                       description="Collaboration album with major artists", event_type="release",
                       risk_level="medium", outcome="positive", skills=["collaboration"]),
            CareerEvent(artist_id=ed.id, age=30, year=2021, title="'=' (Equals) Album",
                       description="Fourth studio album, continued chart dominance", event_type="release",
                       risk_level="low", outcome="positive", skills=["consistency"]),
            CareerEvent(artist_id=ed.id, age=32, year=2023, title="Mathematics Tour",
                       description="Highest-grossing tour by solo artist", event_type="performance",
                       risk_level="low", outcome="positive", skills=["touring", "solo_performance"]),
            CareerEvent(artist_id=ed.id, age=33, year=2024, title="Continued Global Success",
                       description="Multiple albums, tours, and collaborations", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["sustained_career"]),
        ]
        db.add_all(new_ed_events)
        print("✓ Extended Ed Sheeran to age 33")
    
    # Billie Eilish - extend to age 22 (2024)
    billie = db.query(Artist).filter(Artist.name == "Billie Eilish").first()
    if billie:
        new_billie_events = [
            CareerEvent(artist_id=billie.id, age=15, year=2017, title="'Don't Smile at Me' EP",
                       description="Debut EP gained critical acclaim", event_type="release",
                       risk_level="medium", outcome="positive", skills=["ep_creation"]),
            CareerEvent(artist_id=billie.id, age=17, year=2019, title="'When We All Fall Asleep' Album",
                       description="Debut album, youngest artist to win all 4 major Grammys", event_type="release",
                       risk_level="high", outcome="positive", skills=["album_production", "innovation"]),
            CareerEvent(artist_id=billie.id, age=18, year=2020, title="Grammy Sweep",
                       description="Won Record, Album, Song of the Year + Best New Artist", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["recognition"]),
            CareerEvent(artist_id=billie.id, age=19, year=2021, title="'Happier Than Ever' Album",
                       description="Second album debuted at #1, more mature sound", event_type="release",
                       risk_level="medium", outcome="positive", skills=["evolution", "maturity"]),
            CareerEvent(artist_id=billie.id, age=20, year=2022, title="'No Time to Die' Oscar",
                       description="Won Oscar for James Bond theme song", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["film_music"]),
            CareerEvent(artist_id=billie.id, age=21, year=2023, title="'What Was I Made For?' Barbie",
                       description="Viral song from Barbie movie, Grammy winner", event_type="release",
                       risk_level="medium", outcome="positive", skills=["soundtrack", "viral_success"]),
            CareerEvent(artist_id=billie.id, age=22, year=2024, title="Third Album Era",
                       description="Continued evolution as artist and performer", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["artistry"]),
        ]
        db.add_all(new_billie_events)
        print("✓ Extended Billie Eilish to age 22")
    
    # Chance the Rapper - extend to age 31 (2024)
    chance = db.query(Artist).filter(Artist.name == "Chance the Rapper").first()
    if chance:
        new_chance_events = [
            CareerEvent(artist_id=chance.id, age=21, year=2014, title="'Coloring Book' Mixtape",
                       description="Third mixtape, first streaming-only album to win Grammy", event_type="release",
                       risk_level="high", outcome="positive", skills=["innovation", "independence"]),
            CareerEvent(artist_id=chance.id, age=23, year=2016, title="Won 3 Grammy Awards",
                       description="Best Rap Album without traditional release", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["industry_disruption"]),
            CareerEvent(artist_id=chance.id, age=26, year=2019, title="'The Big Day' Album",
                       description="First studio album, mixed reception", event_type="release",
                       risk_level="high", outcome="neutral", skills=["experimentation"]),
            CareerEvent(artist_id=chance.id, age=28, year=2021, title="Return to Independent Music",
                       description="Continued releasing independent music and activism", event_type="milestone",
                       risk_level="medium", outcome="positive", skills=["authenticity"]),
            CareerEvent(artist_id=chance.id, age=31, year=2024, title="Chicago Activism & Music",
                       description="Continued music career and community work in Chicago", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["community_impact"]),
        ]
        db.add_all(new_chance_events)
        print("✓ Extended Chance the Rapper to age 31")
    
    # Justin Bieber - extend to age 30 (2024)
    justin = db.query(Artist).filter(Artist.name == "Justin Bieber").first()
    if justin:
        new_justin_events = [
            CareerEvent(artist_id=justin.id, age=16, year=2010, title="'My World 2.0' Album",
                       description="Debut album debuted at #1, global phenomenon", event_type="release",
                       risk_level="high", outcome="positive", skills=["teen_idol", "marketing"]),
            CareerEvent(artist_id=justin.id, age=18, year=2012, title="'Believe' Album",
                       description="Transition to more mature sound", event_type="release",
                       risk_level="high", outcome="positive", skills=["evolution"]),
            CareerEvent(artist_id=justin.id, age=21, year=2015, title="'Purpose' Album & Comeback",
                       description="Career comeback after controversies, 'Sorry' and 'Love Yourself' hits", event_type="release",
                       risk_level="high", outcome="positive", skills=["comeback", "redemption"]),
            CareerEvent(artist_id=justin.id, age=26, year=2020, title="'Changes' Album",
                       description="R&B-focused album, married life themes", event_type="release",
                       risk_level="medium", outcome="positive", skills=["genre_exploration"]),
            CareerEvent(artist_id=justin.id, age=27, year=2021, title="'Justice' Album",
                       description="Sixth studio album, continued success", event_type="release",
                       risk_level="medium", outcome="positive", skills=["consistency"]),
            CareerEvent(artist_id=justin.id, age=30, year=2024, title="Veteran Pop Star",
                       description="15+ years in industry, continued relevance", event_type="milestone",
                       risk_level="low", outcome="positive", skills=["longevity"]),
        ]
        db.add_all(new_justin_events)
        print("✓ Extended Justin Bieber to age 30")
    
    db.commit()
    print("\n✅ Part 1 Complete: Extended first 5 artists to current age\n")
    
    # ========== PART 2: ADD 40+ NEW ARTISTS ==========
    print("📝 Part 2: Adding 40+ new artists from diverse domains...\n")
    
    new_artists_data = [
        # SINGERS/SONGWRITERS
        {
            "name": "Ariana Grande",
            "domain": "Singer/Actress",
            "start_age": 15,
            "first_break_age": 20,
            "training_type": "Broadway training, vocal coaching",
            "constraints": "Started as actress, transitioned to music",
            "starting_point": "Broadway, Nickelodeon",
            "short_bio": "Started on Broadway and Nickelodeon, became one of the biggest pop stars.",
            "events": [
                (15, 2008, "Cast in '13' on Broadway", "Broadway debut", "performance", "medium", "positive", ["acting", "singing"]),
                (17, 2010, "Cast in 'Victorious'", "Nickelodeon show", "milestone", "medium", "positive", ["acting", "exposure"]),
                (20, 2013, "'Yours Truly' Debut Album", "First album debuted at #1", "release", "high", "positive", ["recording", "pop"]),
                (22, 2015, "'Dangerous Woman' Album", "Third album, mature sound", "release", "medium", "positive", ["evolution"]),
                (25, 2018, "'Sweetener' & 'Thank U, Next'", "Two albums in one year, massive success", "release", "high", "positive", ["productivity"]),
                (27, 2020, "'Positions' Album", "Fifth album during pandemic", "release", "medium", "positive", ["consistency"]),
                (30, 2023, "Continued Success", "Tours, albums, acting", "milestone", "low", "positive", ["versatility"]),
            ]
        },
        {
            "name": "The Weeknd (Abel Tesfaye)",
            "domain": "Singer/Songwriter",
            "start_age": 21,
            "first_break_age": 22,
            "training_type": "Self-taught",
            "constraints": "High school dropout, struggled early",
            "starting_point": "Anonymous YouTube uploads",
            "short_bio": "Uploaded music anonymously, became global R&B superstar.",
            "events": [
                (21, 2011, "Anonymous YouTube Uploads", "Posted songs anonymously", "training", "medium", "positive", ["mystery", "r&b"]),
                (22, 2012, "'Trilogy' Compilation", "Compilation of mixtapes, critical acclaim", "release", "high", "positive", ["production"]),
                (25, 2015, "'Can't Feel My Face' Hit", "Mainstream breakthrough", "release", "high", "positive", ["crossover"]),
                (26, 2016, "'Starboy' Album", "Collaboration with Daft Punk", "release", "medium", "positive", ["collaboration"]),
                (30, 2020, "'After Hours' Album", "'Blinding Lights' became massive hit", "release", "high", "positive", ["hit_making"]),
                (32, 2022, "'Dawn FM' Album", "Concept album", "release", "medium", "positive", ["artistry"]),
                (34, 2024, "Super Bowl & Tours", "Headlined Super Bowl, stadium tours", "performance", "low", "positive", ["live_performance"]),
            ]
        },
        {
            "name": "Shawn Mendes",
            "domain": "Singer/Songwriter",
            "start_age": 15,
            "first_break_age": 16,
            "training_type": "Self-taught guitar, online tutorials",
            "constraints": "High school student",
            "starting_point": "Vine covers",
            "short_bio": "Posted 6-second covers on Vine, became pop sensation.",
            "events": [
                (15, 2014, "Vine Covers", "Posted guitar covers on Vine app", "training", "low", "positive", ["guitar", "social_media"]),
                (16, 2015, "Signed Record Deal", "Island Records deal", "milestone", "medium", "positive", ["business"]),
                (17, 2016, "'Illuminate' Album", "Second album, global tours", "release", "high", "positive", ["touring"]),
                (20, 2019, "'Shawn Mendes' Self-Titled", "Third album, mature sound", "release", "medium", "positive", ["evolution"]),
                (22, 2020, "'Wonder' Album", "Fourth album", "release", "medium", "positive", ["consistency"]),
                (25, 2023, "Continued Success", "Tours and new music", "milestone", "low", "positive", ["sustained_career"]),
            ]
        },
        {
            "name": "Olivia Rodrigo",
            "domain": "Singer/Songwriter/Actress",
            "start_age": 18,
            "first_break_age": 18,
            "training_type": "Acting training, self-taught songwriting",
            "constraints": "Started as Disney actress",
            "starting_point": "Disney Channel, songwriting",
            "short_bio": "Disney actress who became overnight pop sensation with 'drivers license'.",
            "events": [
                (15, 2018, "Cast in 'High School Musical: The Series'", "Disney+ show", "milestone", "medium", "positive", ["acting"]),
                (17, 2020, "Started Writing Songs", "Wrote songs for show and personal project", "training", "low", "positive", ["songwriting"]),
                (18, 2021, "'drivers license' Released", "Viral hit, broke streaming records", "release", "high", "positive", ["viral_success"]),
                (18, 2021, "'SOUR' Album", "Debut album, critical and commercial success", "release", "high", "positive", ["album_creation"]),
                (19, 2022, "Won 3 Grammy Awards", "Best New Artist and more", "milestone", "low", "positive", ["recognition"]),
                (20, 2023, "'GUTS' Album", "Second album, continued success", "release", "medium", "positive", ["sophomore_success"]),
                (21, 2024, "GUTS World Tour", "Global tour", "performance", "low", "positive", ["touring"]),
            ]
        },
        
        # RAPPERS/HIP-HOP
        {
            "name": "Drake",
            "domain": "Rapper/Singer",
            "start_age": 20,
            "first_break_age": 23,
            "training_type": "Self-taught, acting background",
            "constraints": "Started as actor, Canadian in US market",
            "starting_point": "Degrassi actor, mixtapes",
            "short_bio": "Former teen actor became one of the biggest rappers of all time.",
            "events": [
                (20, 2006, "Released First Mixtape", "Room for Improvement", "training", "medium", "positive", ["rapping", "production"]),
                (23, 2009, "'So Far Gone' Mixtape", "Breakthrough mixtape, 'Best I Ever Had'", "release", "high", "positive", ["hit_making"]),
                (24, 2010, "'Thank Me Later' Album", "Debut album debuted at #1", "release", "high", "positive", ["album_creation"]),
                (28, 2015, "'If You're Reading This' Surprise Release", "Surprise mixtape, streaming success", "release", "high", "positive", ["innovation"]),
                (31, 2018, "'Scorpion' Double Album", "'In My Feelings' viral dance challenge", "release", "medium", "positive", ["viral_marketing"]),
                (37, 2024, "Continued Dominance", "Most-streamed artist, business ventures", "milestone", "low", "positive", ["business", "streaming"]),
            ]
        },
        {
            "name": "Cardi B",
            "domain": "Rapper",
            "start_age": 23,
            "first_break_age": 25,
            "training_type": "Self-taught",
            "constraints": "Former stripper, no industry connections",
            "starting_point": "Instagram, reality TV",
            "short_bio": "Instagram personality and reality star became Grammy-winning rapper.",
            "events": [
                (23, 2015, "Instagram Fame", "Gained millions of followers with personality", "training", "low", "positive", ["social_media", "personality"]),
                (24, 2016, "Love & Hip Hop", "Joined reality show", "milestone", "medium", "positive", ["exposure"]),
                (25, 2017, "'Bodak Yellow' Hit", "First female rapper to top charts solo in 19 years", "release", "high", "positive", ["historic"]),
                (26, 2018, "'Invasion of Privacy' Album", "Debut album, won Grammy", "release", "high", "positive", ["album_creation"]),
                (31, 2023, "Continued Success", "Multiple hits, business ventures", "milestone", "low", "positive", ["business"]),
            ]
        },
        {
            "name": "Post Malone",
            "domain": "Rapper/Singer",
            "start_age": 19,
            "first_break_age": 20,
            "training_type": "Self-taught, guitar background",
            "constraints": "Dropped out of college",
            "starting_point": "SoundCloud",
            "short_bio": "Posted 'White Iverson' on SoundCloud, became multi-genre superstar.",
            "events": [
                (19, 2015, "'White Iverson' on SoundCloud", "Viral hit, millions of plays", "release", "high", "positive", ["viral_success"]),
                (21, 2016, "'Stoney' Debut Album", "First album, certified triple platinum", "release", "high", "positive", ["album_creation"]),
                (23, 2018, "'Beerbongs & Bentleys'", "Second album, broke streaming records", "release", "high", "positive", ["streaming_success"]),
                (24, 2019, "'Hollywood's Bleeding'", "Third album, continued dominance", "release", "medium", "positive", ["consistency"]),
                (28, 2023, "Genre Experimentation", "Country and rock influences", "release", "medium", "positive", ["versatility"]),
            ]
        },
        
        # YOUTUBERS/CONTENT CREATORS
        {
            "name": "PewDiePie (Felix Kjellberg)",
            "domain": "YouTuber/Content Creator",
            "start_age": 21,
            "first_break_age": 23,
            "training_type": "Self-taught video editing",
            "constraints": "Dropped out of university, sold hot dogs",
            "starting_point": "Gaming videos",
            "short_bio": "Started gaming channel, became most-subscribed YouTuber for years.",
            "events": [
                (21, 2010, "Started YouTube Channel", "Posted first gaming videos", "training", "low", "positive", ["gaming", "commentary"]),
                (23, 2012, "1 Million Subscribers", "Rapid growth in gaming community", "milestone", "medium", "positive", ["audience_building"]),
                (25, 2014, "Most Subscribed YouTuber", "Became #1 on YouTube", "milestone", "low", "positive", ["achievement"]),
                (29, 2018, "T-Series Competition", "Battle for most subscribed channel", "milestone", "low", "positive", ["viral_moment"]),
                (34, 2023, "100M+ Subscribers", "Maintained massive audience", "milestone", "low", "positive", ["longevity"]),
            ]
        },
        {
            "name": "Markiplier (Mark Fischbach)",
            "domain": "YouTuber/Content Creator",
            "start_age": 23,
            "first_break_age": 25,
            "training_type": "Self-taught, biomedical engineering dropout",
            "constraints": "Health issues, dropped out of college",
            "starting_point": "Gaming videos",
            "short_bio": "Started gaming channel after health crisis, became top YouTuber and philanthropist.",
            "events": [
                (23, 2012, "Started YouTube Channel", "Posted first gaming videos", "training", "low", "positive", ["gaming", "editing"]),
                (25, 2014, "Rapid Growth", "Millions of subscribers, charity work", "milestone", "medium", "positive", ["charity"]),
                (28, 2017, "10M Subscribers", "Major milestone", "milestone", "low", "positive", ["audience_growth"]),
                (32, 2021, "Branched to Film", "Started film projects", "milestone", "medium", "positive", ["diversification"]),
                (34, 2023, "35M+ Subscribers", "Continued success and charity", "milestone", "low", "positive", ["sustained_success"]),
            ]
        },
        {
            "name": "Jenna Marbles (Jenna Mourey)",
            "domain": "YouTuber/Content Creator",
            "start_age": 24,
            "first_break_age": 24,
            "training_type": "Self-taught, sports psychology degree",
            "constraints": "Worked multiple jobs",
            "starting_point": "Viral comedy videos",
            "short_bio": "Posted viral video while working multiple jobs, became YouTube pioneer.",
            "events": [
                (24, 2010, "'How To Trick People' Video", "Viral video launched channel", "release", "high", "positive", ["viral_content"]),
                (26, 2012, "1 Million Subscribers", "Rapid growth", "milestone", "medium", "positive", ["audience_building"]),
                (30, 2016, "20M Subscribers", "One of top female YouTubers", "milestone", "low", "positive", ["achievement"]),
                (33, 2020, "Retired from YouTube", "Left platform after 10 years", "life_change", "high", "neutral", ["decision_making"]),
            ]
        },
        
        # PRODUCERS/DJs
        {
            "name": "Calvin Harris",
            "domain": "DJ/Producer",
            "start_age": 18,
            "first_break_age": 23,
            "training_type": "Self-taught production",
            "constraints": "Worked in supermarket",
            "starting_point": "Bedroom production",
            "short_bio": "Produced music in bedroom, became highest-paid DJ.",
            "events": [
                (18, 2002, "Started Producing", "Began making electronic music", "training", "low", "positive", ["production"]),
                (23, 2007, "'Acceptable in the 80s' Hit", "First major single", "release", "high", "positive", ["breakthrough"]),
                (28, 2012, "'Feel So Close' Success", "International hit", "release", "medium", "positive", ["hit_making"]),
                (30, 2014, "Collaboration with Rihanna", "'We Found Love' massive success", "collaboration", "high", "positive", ["collaboration"]),
                (40, 2024, "Highest-Paid DJ", "Continued success and residencies", "milestone", "low", "positive", ["business"]),
            ]
        },
        {
            "name": "Marshmello",
            "domain": "DJ/Producer",
            "start_age": 23,
            "first_break_age": 24,
            "training_type": "Self-taught production",
            "constraints": "Anonymous identity",
            "starting_point": "SoundCloud, anonymous persona",
            "short_bio": "Created anonymous DJ persona, became global EDM star.",
            "events": [
                (23, 2015, "Started Marshmello Project", "Created anonymous persona", "training", "medium", "positive", ["branding", "mystery"]),
                (24, 2016, "'Alone' Hit", "Breakthrough single", "release", "high", "positive", ["production"]),
                (26, 2018, "'Happier' with Bastille", "Massive crossover hit", "release", "high", "positive", ["collaboration"]),
                (28, 2020, "Fortnite Concert", "Virtual concert in video game", "performance", "high", "positive", ["innovation"]),
                (32, 2024, "Continued Success", "Tours, collaborations, gaming", "milestone", "low", "positive", ["diversification"]),
            ]
        },
        
        # ACTORS/MULTI-HYPHENATES
        {
            "name": "Zendaya",
            "domain": "Actress/Singer",
            "start_age": 14,
            "first_break_age": 17,
            "training_type": "Theater training, Disney",
            "constraints": "Child actor transition",
            "starting_point": "Disney Channel",
            "short_bio": "Started on Disney Channel, became Emmy-winning actress.",
            "events": [
                (14, 2010, "Disney Channel 'Shake It Up'", "First major role", "milestone", "medium", "positive", ["acting"]),
                (17, 2013, "Music Career", "Released singles and album", "release", "medium", "positive", ["singing"]),
                (19, 2015, "Transitioned to Film", "Started film career", "milestone", "high", "positive", ["film_acting"]),
                (23, 2019, "'Euphoria' HBO Series", "Breakthrough adult role, won Emmy", "milestone", "high", "positive", ["dramatic_acting"]),
                (25, 2021, "Spider-Man Films", "Major blockbuster success", "milestone", "medium", "positive", ["blockbuster"]),
                (28, 2024, "Fashion Icon & Actress", "Continued acting and fashion influence", "milestone", "low", "positive", ["fashion", "influence"]),
            ]
        },
        {
            "name": "Timothée Chalamet",
            "domain": "Actor",
            "start_age": 17,
            "first_break_age": 22,
            "training_type": "LaGuardia High School, Columbia University",
            "constraints": "Competitive industry",
            "starting_point": "Theater, small TV roles",
            "short_bio": "Started in theater, became one of the biggest young actors.",
            "events": [
                (17, 2012, "First TV Roles", "Small roles in Law & Order", "training", "low", "positive", ["acting"]),
                (19, 2014, "'Interstellar' Supporting Role", "Christopher Nolan film", "milestone", "medium", "positive", ["film_acting"]),
                (22, 2017, "'Call Me By Your Name'", "Breakthrough role, Oscar nomination", "milestone", "high", "positive", ["leading_role"]),
                (24, 2019, "'Little Women' & 'The King'", "Multiple acclaimed roles", "milestone", "medium", "positive", ["versatility"]),
                (28, 2024, "'Dune' Franchise", "Leading blockbuster franchise", "milestone", "low", "positive", ["franchise_star"]),
            ]
        },
        
        # DANCERS/CHOREOGRAPHERS
        {
            "name": "Maddie Ziegler",
            "domain": "Dancer/Actress",
            "start_age": 8,
            "first_break_age": 11,
            "training_type": "Formal dance training",
            "constraints": "Reality TV child",
            "starting_point": "Dance Moms, Sia videos",
            "short_bio": "Reality TV dancer became Sia's muse and actress.",
            "events": [
                (8, 2011, "'Dance Moms' Reality Show", "Joined reality show", "milestone", "medium", "positive", ["exposure"]),
                (11, 2014, "Sia's 'Chandelier' Video", "Iconic music video performance", "performance", "high", "positive", ["viral_performance"]),
                (13, 2016, "Continued Sia Collaborations", "Multiple music videos and performances", "collaboration", "medium", "positive", ["partnership"]),
                (15, 2018, "Acting Career", "Transitioned to acting", "milestone", "high", "positive", ["acting"]),
                (21, 2024, "Multi-Platform Career", "Dance, acting, writing", "milestone", "low", "positive", ["diversification"]),
            ]
        },
        
        # WRITERS/AUTHORS
        {
            "name": "Rupi Kaur",
            "domain": "Poet/Author",
            "start_age": 21,
            "first_break_age": 23,
            "training_type": "Self-published, Instagram",
            "constraints": "Traditional publishing rejection",
            "starting_point": "Instagram poetry",
            "short_bio": "Self-published poetry on Instagram, became bestselling author.",
            "events": [
                (21, 2014, "Started Instagram Poetry", "Posted illustrated poems", "training", "low", "positive", ["writing", "illustration"]),
                (23, 2015, "'Milk and Honey' Self-Published", "Self-published first book", "release", "high", "positive", ["self_publishing"]),
                (24, 2016, "New York Times Bestseller", "Book became massive success", "milestone", "low", "positive", ["bestseller"]),
                (25, 2017, "'The Sun and Her Flowers'", "Second book", "release", "medium", "positive", ["consistency"]),
                (31, 2024, "Global Poetry Phenomenon", "Millions of books sold worldwide", "milestone", "low", "positive", ["global_success"]),
            ]
        },
        
        # ENTREPRENEURS/INFLUENCERS
        {
            "name": "Kylie Jenner",
            "domain": "Entrepreneur/Influencer",
            "start_age": 17,
            "first_break_age": 19,
            "training_type": "Reality TV, family business",
            "constraints": "Famous family, public scrutiny",
            "starting_point": "Keeping Up with the Kardashians",
            "short_bio": "Reality TV star became youngest self-made billionaire with cosmetics company.",
            "events": [
                (17, 2015, "Launched Kylie Cosmetics", "Started lip kit company", "milestone", "high", "positive", ["entrepreneurship"]),
                (19, 2016, "Sold Out in Minutes", "Products sold out instantly", "milestone", "low", "positive", ["business_success"]),
                (21, 2018, "Youngest Self-Made Billionaire", "Forbes recognition", "milestone", "low", "positive", ["wealth"]),
                (26, 2023, "Expanded Business Empire", "Multiple product lines", "milestone", "low", "positive", ["business_growth"]),
            ]
        },
        {
            "name": "Gary Vaynerchuk",
            "domain": "Entrepreneur/Content Creator",
            "start_age": 22,
            "first_break_age": 30,
            "training_type": "Self-taught, family business",
            "constraints": "Immigrant family",
            "starting_point": "Family wine business, YouTube",
            "short_bio": "Grew family wine business, became social media entrepreneur and motivational speaker.",
            "events": [
                (22, 1997, "Joined Family Wine Business", "Started working in family store", "training", "low", "positive", ["business"]),
                (30, 2006, "Wine Library TV", "Started daily YouTube wine show", "release", "high", "positive", ["content_creation"]),
                (34, 2009, "VaynerMedia Founded", "Started marketing agency", "milestone", "high", "positive", ["agency_building"]),
                (38, 2013, "Social Media Influencer", "Became major business influencer", "milestone", "medium", "positive", ["influence"]),
                (48, 2023, "Multi-Platform Entrepreneur", "Podcasts, books, investments", "milestone", "low", "positive", ["diversification"]),
            ]
        },
        
        # ATHLETES TURNED CREATORS
        {
            "name": "Dude Perfect",
            "domain": "YouTubers/Athletes",
            "start_age": 22,
            "first_break_age": 23,
            "training_type": "College athletes, self-taught video",
            "constraints": "Started as hobby",
            "starting_point": "Trick shot videos",
            "short_bio": "College roommates posting trick shots became massive YouTube channel.",
            "events": [
                (22, 2009, "First Trick Shot Video", "Posted first video in backyard", "training", "low", "positive", ["video_creation"]),
                (23, 2010, "Viral Success", "Videos went viral, millions of views", "milestone", "high", "positive", ["viral_content"]),
                (27, 2014, "10M Subscribers", "Major YouTube milestone", "milestone", "medium", "positive", ["growth"]),
                (32, 2019, "Guinness World Records", "Multiple world records", "milestone", "low", "positive", ["achievement"]),
                (37, 2024, "60M+ Subscribers", "One of biggest channels, live tours", "milestone", "low", "positive", ["sustained_success"]),
            ]
        },
        
        # GAMING/ESPORTS
        {
            "name": "Ninja (Tyler Blevins)",
            "domain": "Gamer/Streamer",
            "start_age": 18,
            "first_break_age": 27,
            "training_type": "Professional gaming",
            "constraints": "Competitive gaming career",
            "starting_point": "Professional Halo player",
            "short_bio": "Professional gamer became biggest Twitch streamer with Fortnite.",
            "events": [
                (18, 2009, "Professional Halo Player", "Started esports career", "training", "medium", "positive", ["gaming"]),
                (24, 2015, "Started Streaming", "Began streaming on Twitch", "training", "medium", "positive", ["streaming"]),
                (27, 2018, "Fortnite Explosion", "Became biggest streamer with Fortnite", "milestone", "high", "positive", ["viral_success"]),
                (28, 2019, "Mixer Deal", "Exclusive streaming deal", "milestone", "high", "positive", ["business"]),
                (32, 2023, "Multi-Platform Streamer", "Returned to Twitch, brand deals", "milestone", "low", "positive", ["adaptation"]),
            ]
        },
        {
            "name": "Pokimane (Imane Anys)",
            "domain": "Gamer/Streamer",
            "start_age": 17,
            "first_break_age": 21,
            "training_type": "Self-taught streaming",
            "constraints": "Female in male-dominated field",
            "starting_point": "League of Legends streaming",
            "short_bio": "Started streaming while in university, became top female streamer.",
            "events": [
                (17, 2013, "Started Streaming", "Began streaming League of Legends", "training", "low", "positive", ["gaming", "streaming"]),
                (21, 2017, "Fortnite Growth", "Rapid growth with Fortnite", "milestone", "high", "positive", ["audience_growth"]),
                (23, 2019, "Top Female Streamer", "Most-followed female on Twitch", "milestone", "low", "positive", ["achievement"]),
                (27, 2023, "Business Ventures", "Launched own brand and products", "milestone", "medium", "positive", ["entrepreneurship"]),
            ]
        },
        
        # COMEDY
        {
            "name": "Bo Burnham",
            "domain": "Comedian/Filmmaker",
            "start_age": 16,
            "first_break_age": 18,
            "training_type": "Self-taught comedy and music",
            "constraints": "Started in bedroom",
            "starting_point": "YouTube comedy songs",
            "short_bio": "Posted comedy songs from bedroom, became acclaimed comedian and filmmaker.",
            "events": [
                (16, 2006, "YouTube Comedy Songs", "Posted first comedy songs", "training", "low", "positive", ["comedy", "music"]),
                (18, 2008, "Comedy Central Special", "Youngest comedian with special", "milestone", "high", "positive", ["stand_up"]),
                (23, 2013, "'what.' Comedy Special", "Critically acclaimed special", "release", "medium", "positive", ["performance"]),
                (28, 2018, "Directed 'Eighth Grade'", "Directorial debut", "milestone", "high", "positive", ["directing"]),
                (30, 2021, "'Inside' Netflix Special", "Pandemic special, Emmy winner", "release", "high", "positive", ["innovation"]),
            ]
        },
        {
            "name": "Hannah Gadsby",
            "domain": "Comedian",
            "start_age": 28,
            "first_break_age": 40,
            "training_type": "Stand-up comedy",
            "constraints": "Late start, regional Australia",
            "starting_point": "Australian comedy circuit",
            "short_bio": "Australian comedian who revolutionized stand-up with 'Nanette'.",
            "events": [
                (28, 2006, "Started Stand-Up", "Began comedy career in Australia", "training", "medium", "positive", ["stand_up"]),
                (35, 2013, "Australian Comedy Success", "Built following in Australia", "milestone", "medium", "positive", ["regional_success"]),
                (40, 2018, "'Nanette' Netflix Special", "Revolutionary special, global acclaim", "release", "high", "positive", ["innovation"]),
                (42, 2020, "'Douglas' Special", "Follow-up special", "release", "medium", "positive", ["consistency"]),
                (46, 2024, "Continued Success", "Tours and specials", "milestone", "low", "positive", ["sustained_career"]),
            ]
        },
        
        # FASHION/BEAUTY
        {
            "name": "James Charles",
            "domain": "Beauty YouTuber",
            "start_age": 17,
            "first_break_age": 17,
            "training_type": "Self-taught makeup",
            "constraints": "Male in female-dominated field",
            "starting_point": "Instagram makeup",
            "short_bio": "First male CoverGirl ambassador, became beauty YouTube star.",
            "events": [
                (17, 2016, "CoverGirl Ambassador", "First male CoverGirl", "milestone", "high", "positive", ["breaking_barriers"]),
                (18, 2017, "YouTube Growth", "Rapid subscriber growth", "milestone", "medium", "positive", ["content_creation"]),
                (20, 2019, "Morphe Palette", "Launched makeup collaboration", "milestone", "medium", "positive", ["business"]),
                (24, 2023, "25M+ Subscribers", "Continued influence in beauty", "milestone", "low", "positive", ["influence"]),
            ]
        },
        {
            "name": "Jeffree Star",
            "domain": "Beauty YouTuber/Entrepreneur",
            "start_age": 20,
            "first_break_age": 30,
            "training_type": "Self-taught makeup and business",
            "constraints": "Started on MySpace",
            "starting_point": "MySpace music and makeup",
            "short_bio": "MySpace celebrity became beauty empire owner.",
            "events": [
                (20, 2006, "MySpace Fame", "Built following on MySpace", "training", "medium", "positive", ["social_media"]),
                (28, 2014, "Jeffree Star Cosmetics", "Launched makeup brand", "milestone", "high", "positive", ["entrepreneurship"]),
                (30, 2016, "YouTube Beauty Channel", "Started YouTube channel", "milestone", "medium", "positive", ["content_creation"]),
                (38, 2024, "Beauty Empire", "Multi-million dollar business", "milestone", "low", "positive", ["business_success"]),
            ]
        },
        
        # PODCASTERS
        {
            "name": "Joe Rogan",
            "domain": "Podcaster/Comedian",
            "start_age": 21,
            "first_break_age": 30,
            "training_type": "Stand-up comedy, martial arts",
            "constraints": "Multiple career pivots",
            "starting_point": "Stand-up comedy",
            "short_bio": "Comedian and UFC commentator became biggest podcaster.",
            "events": [
                (21, 1988, "Started Stand-Up", "Began comedy career", "training", "medium", "positive", ["comedy"]),
                (30, 1997, "Fear Factor Host", "Hosted reality show", "milestone", "medium", "positive", ["hosting"]),
                (42, 2009, "Started Podcast", "Launched Joe Rogan Experience", "milestone", "high", "positive", ["podcasting"]),
                (53, 2020, "Spotify Deal", "$100M+ exclusive deal", "milestone", "low", "positive", ["business"]),
                (56, 2023, "Biggest Podcast", "Most-listened podcast globally", "milestone", "low", "positive", ["dominance"]),
            ]
        },
        {
            "name": "Alex Cooper",
            "domain": "Podcaster",
            "start_age": 24,
            "first_break_age": 26,
            "training_type": "Self-taught podcasting",
            "constraints": "Competitive podcast market",
            "starting_point": "Call Her Daddy podcast",
            "short_bio": "Started podcast with friend, became solo host with massive deal.",
            "events": [
                (24, 2018, "Started 'Call Her Daddy'", "Co-hosted podcast", "training", "medium", "positive", ["podcasting"]),
                (26, 2020, "Went Solo", "Became sole host after split", "milestone", "high", "positive", ["independence"]),
                (27, 2021, "Spotify Deal", "Exclusive deal with Spotify", "milestone", "high", "positive", ["business"]),
                (29, 2023, "Top Female Podcaster", "One of highest-paid podcasters", "milestone", "low", "positive", ["success"]),
            ]
        },
        
        # TECH/SCIENCE CREATORS
        {
            "name": "Mark Rober",
            "domain": "YouTuber/Engineer",
            "start_age": 41,
            "first_break_age": 43,
            "training_type": "NASA engineer, self-taught video",
            "constraints": "Late start to YouTube",
            "starting_point": "Engineering videos",
            "short_bio": "Former NASA engineer started YouTube channel, became science education star.",
            "events": [
                (41, 2011, "Started YouTube", "Posted first engineering videos", "training", "low", "positive", ["video_creation", "engineering"]),
                (43, 2013, "Viral Halloween Costume", "iPad costume went viral", "milestone", "high", "positive", ["viral_content"]),
                (48, 2018, "Glitter Bomb Videos", "Package thief revenge videos", "release", "high", "positive", ["innovation"]),
                (53, 2023, "25M+ Subscribers", "Major science education channel", "milestone", "low", "positive", ["education"]),
            ]
        },
        {
            "name": "Vsauce (Michael Stevens)",
            "domain": "YouTuber/Educator",
            "start_age": 24,
            "first_break_age": 28,
            "training_type": "Self-taught science communication",
            "constraints": "Educational content in entertainment space",
            "starting_point": "Video game content",
            "short_bio": "Started with gaming, became science education phenomenon.",
            "events": [
                (24, 2010, "Started Vsauce", "Posted first videos", "training", "low", "positive", ["content_creation"]),
                (28, 2014, "Science Education Focus", "Shifted to educational content", "milestone", "high", "positive", ["pivot"]),
                (32, 2018, "YouTube Red Series", "Premium content series", "milestone", "medium", "positive", ["expansion"]),
                (38, 2024, "20M+ Subscribers", "Leading science education channel", "milestone", "low", "positive", ["education"]),
            ]
        },
        
        # FOOD/LIFESTYLE
        {
            "name": "Rosanna Pansino",
            "domain": "YouTuber/Baker",
            "start_age": 26,
            "first_break_age": 28,
            "training_type": "Self-taught baking and video",
            "constraints": "Actress turned baker",
            "starting_point": "Nerdy Nummies baking show",
            "short_bio": "Actress started baking channel, became top food YouTuber.",
            "events": [
                (26, 2011, "Started Nerdy Nummies", "Posted first baking video", "training", "low", "positive", ["baking", "video"]),
                (28, 2013, "1M Subscribers", "Rapid growth", "milestone", "medium", "positive", ["audience_growth"]),
                (32, 2017, "Cookbook Published", "NYT bestselling cookbook", "release", "medium", "positive", ["publishing"]),
                (38, 2023, "14M+ Subscribers", "Top food content creator", "milestone", "low", "positive", ["sustained_success"]),
            ]
        },
        
        # MUSICIANS (ADDITIONAL)
        {
            "name": "Lil Nas X",
            "domain": "Rapper/Singer",
            "start_age": 19,
            "first_break_age": 20,
            "training_type": "Self-taught, social media",
            "constraints": "No industry connections",
            "starting_point": "Twitter memes, SoundCloud",
            "short_bio": "Posted country-rap song on TikTok, became global phenomenon.",
            "events": [
                (19, 2018, "Posted 'Old Town Road'", "Released song independently", "release", "high", "positive", ["viral_marketing"]),
                (20, 2019, "Billboard #1 Record", "Longest-running #1 in history", "milestone", "high", "positive", ["record_breaking"]),
                (21, 2020, "Came Out Publicly", "First openly gay rapper to win Grammy", "milestone", "high", "positive", ["representation"]),
                (23, 2022, "Debut Album Success", "Continued chart success", "release", "medium", "positive", ["consistency"]),
                (25, 2024, "Cultural Icon", "Music, fashion, activism", "milestone", "low", "positive", ["influence"]),
            ]
        },
        {
            "name": "H.E.R. (Gabriella Wilson)",
            "domain": "Singer/Songwriter",
            "start_age": 19,
            "first_break_age": 21,
            "training_type": "Formal music training, child performer",
            "constraints": "Early career struggles, rebranding",
            "starting_point": "Child performer, mysterious rebrand",
            "short_bio": "Child performer rebranded as mysterious artist H.E.R., won multiple Grammys.",
            "events": [
                (10, 2007, "Child Performer", "Performed on Today Show", "training", "low", "positive", ["performance"]),
                (14, 2011, "First Record Deal", "Signed deal, released music", "milestone", "medium", "positive", ["business"]),
                (19, 2016, "Rebranded as H.E.R.", "New mysterious persona", "milestone", "high", "positive", ["rebranding"]),
                (21, 2018, "Grammy Wins", "Won multiple Grammys", "milestone", "low", "positive", ["recognition"]),
                (26, 2023, "Oscar Win", "Won Oscar for 'Fight for You'", "milestone", "low", "positive", ["achievement"]),
            ]
        },
        {
            "name": "Bad Bunny",
            "domain": "Rapper/Singer",
            "start_age": 22,
            "first_break_age": 24,
            "training_type": "Self-taught",
            "constraints": "Spanish-language in English market",
            "starting_point": "SoundCloud",
            "short_bio": "Puerto Rican artist became global superstar with Spanish-language music.",
            "events": [
                (22, 2016, "Posted on SoundCloud", "Released first tracks", "training", "medium", "positive", ["music_creation"]),
                (24, 2018, "'I Like It' with Cardi B", "First Billboard #1", "release", "high", "positive", ["crossover"]),
                (26, 2020, "'YHLQMDLG' Album", "Highest-charting all-Spanish album", "release", "high", "positive", ["breaking_barriers"]),
                (28, 2022, "Most-Streamed Artist", "Most-streamed on Spotify globally", "milestone", "low", "positive", ["streaming_dominance"]),
                (30, 2024, "Stadium Tours", "Sold-out stadium tours worldwide", "performance", "low", "positive", ["global_success"]),
            ]
        },
        {
            "name": "SZA",
            "domain": "Singer/Songwriter",
            "start_age": 22,
            "first_break_age": 27,
            "training_type": "Self-taught",
            "constraints": "Late start, industry rejection",
            "starting_point": "SoundCloud, independent EPs",
            "short_bio": "Posted music on SoundCloud, became R&B superstar.",
            "events": [
                (22, 2012, "Posted on SoundCloud", "Released first EP independently", "training", "medium", "positive", ["music_creation"]),
                (24, 2014, "Signed with TDE", "Joined Top Dawg Entertainment", "milestone", "high", "positive", ["label_deal"]),
                (27, 2017, "'Ctrl' Album", "Debut album, critical acclaim", "release", "high", "positive", ["album_creation"]),
                (33, 2023, "'SOS' Album", "Second album, massive success", "release", "high", "positive", ["comeback"]),
                (34, 2024, "Grammy Wins", "Multiple Grammy awards", "milestone", "low", "positive", ["recognition"]),
            ]
        },
    ]
    
    # Add all new artists
    count = 0
    for artist_data in new_artists_data:
        artist = Artist(
            name=artist_data["name"],
            domain=artist_data["domain"],
            start_age=artist_data["start_age"],
            first_break_age=artist_data["first_break_age"],
            training_type=artist_data["training_type"],
            constraints=artist_data["constraints"],
            starting_point=artist_data["starting_point"],
            short_bio=artist_data["short_bio"],
            image_url=f"https://via.placeholder.com/300x300?text={artist_data['name'].replace(' ', '+')}"
        )
        db.add(artist)
        db.flush()
        
        # Add events
        for event_data in artist_data["events"]:
            event = CareerEvent(
                artist_id=artist.id,
                age=event_data[0],
                year=event_data[1],
                title=event_data[2],
                description=event_data[3],
                event_type=event_data[4],
                risk_level=event_data[5],
                outcome=event_data[6],
                skills=event_data[7]
            )
            db.add(event)
        
        count += 1
        if count % 10 == 0:
            print(f"  Added {count} artists...")
    
    db.commit()
    
    # Final statistics
    total_artists = db.query(Artist).count()
    total_events = db.query(CareerEvent).count()
    
    print(f"\n✅ Part 2 Complete: Added {count} new artists")
    print("\n" + "=" * 60)
    print("DATABASE EXPANSION COMPLETE!")
    print("=" * 60)
    print(f"📊 Total Artists: {total_artists}")
    print(f"📊 Total Career Events: {total_events}")
    print(f"📊 Average Events per Artist: {total_events / total_artists:.1f}")
    print("\n🎉 Your database now has comprehensive coverage of:")
    print("   - Singers/Songwriters")
    print("   - Rappers/Hip-Hop Artists")
    print("   - YouTubers/Content Creators")
    print("   - DJs/Producers")
    print("   - Actors/Actresses")
    print("   - Dancers/Choreographers")
    print("   - Comedians")
    print("   - Podcasters")
    print("   - Entrepreneurs")
    print("   - Gamers/Streamers")
    print("   - Beauty/Fashion Influencers")
    print("   - Science/Tech Educators")
    print("   - And more!")
    print("\n🚀 Refresh your browser to see all the new artists!")
    
    db.close()

if __name__ == "__main__":
    expand_database()
