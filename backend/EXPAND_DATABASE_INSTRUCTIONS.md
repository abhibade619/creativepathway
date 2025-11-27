# Database Expansion Instructions

## 🎯 What This Does

The `expand_database.py` script will:

### Part 1: Extend Original 5 Artists to Current Age
- **Taylor Swift** → age 34 (adds 10 events)
- **Ed Sheeran** → age 33 (adds 8 events)
- **Billie Eilish** → age 22 (adds 7 events)
- **Chance the Rapper** → age 31 (adds 5 events)
- **Justin Bieber** → age 30 (adds 6 events)

### Part 2: Add 40+ New Artists

**Total Result: ~50 artists with 200+ career events**

## 📋 How to Run

### In your Anaconda Prompt (where backend is running):

1. **Stop the backend server**
   ```
   Press Ctrl+C
   ```

2. **Run the expansion script**
   ```bash
   python expand_database.py
   ```
   
   This will take about 30 seconds to add all artists and events.

3. **Restart the backend**
   ```bash
   uvicorn main:app --reload
   ```

4. **Refresh your browser**
   ```
   Go to http://localhost:5174/artists
   ```

## 🎨 New Domains Covered

- Singers/Songwriters (Ariana Grande, The Weeknd, Shawn Mendes, Olivia Rodrigo, SZA, H.E.R., Bad Bunny, Lil Nas X)
- Rappers (Drake, Cardi B, Post Malone)
- YouTubers (PewDiePie, Markiplier, Jenna Marbles, MrBeast, Lilly Singh, Emma Chamberlain)
- DJs/Producers (Calvin Harris, Marshmello, Zedd)
- Actors (Zendaya, Timothée Chalamet, Donald Glover)
- Dancers (Maddie Ziegler)
- Comedians (Bo Burnham, Hannah Gadsby)
- Podcasters (Joe Rogan, Alex Cooper)
- Gamers/Streamers (Ninja, Pokimane, Dude Perfect)
- Beauty Influencers (James Charles, Jeffree Star)
- Entrepreneurs (Kylie Jenner, Gary Vaynerchuk)
- Science Educators (Mark Rober, Vsauce)
- Food Creators (Rosanna Pansino)
- Writers (Rupi Kaur)

## ✅ Expected Output

You should see:
```
==========================================================
EXPANDING CREATIVE PATHWAYS DATABASE
==========================================================

📝 Part 1: Extending existing artists to current age...
✓ Extended Taylor Swift to age 34
✓ Extended Ed Sheeran to age 33
✓ Extended Billie Eilish to age 22
✓ Extended Chance the Rapper to age 31
✓ Extended Justin Bieber to age 30

✅ Part 1 Complete: Extended first 5 artists to current age

📝 Part 2: Adding 40+ new artists from diverse domains...
  Added 10 artists...
  Added 20 artists...
  Added 30 artists...
  Added 40 artists...

✅ Part 2 Complete: Added 40 new artists

==========================================================
DATABASE EXPANSION COMPLETE!
==========================================================
📊 Total Artists: ~50
📊 Total Career Events: 200+
📊 Average Events per Artist: ~4-5
```

## 🎉 What You'll Have

A comprehensive database perfect for your capstone project with:
- Diverse creative domains
- Complete career timelines to current age
- Rich matching possibilities
- Detailed roadmap generation data

Ready to run? Just follow the 4 steps above!
