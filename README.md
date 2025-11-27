# Creative Pathways Explorer

An interactive platform that helps aspiring creators find their path by matching them with successful artists who started in similar circumstances.

## 🌟 Features

- **Artist Database**: 50+ artists from diverse creative domains
- **Smart Matching**: AI-powered matching based on age, domain, experience, and constraints
- **Personalized Roadmaps**: 12-month action plans inspired by successful creators
- **Interactive Timelines**: Visual career progression with events, skills, and milestones
- **Domain Filtering**: Browse artists by category (Singers, Rappers, YouTubers, DJs, etc.)

## 🚀 Live Demo

Visit: [Creative Pathways Explorer](https://creativepathway.vercel.app)

## 🛠️ Tech Stack

**Backend:**
- FastAPI (Python)
- SQLAlchemy ORM
- SQLite Database

**Frontend:**
- React 18
- Vite
- TailwindCSS
- React Router
- Axios

## 📦 Local Development

### Prerequisites
- Python 3.8+
- Node.js 16+
- Conda (recommended) or pip

### Backend Setup

```bash
cd backend

# Using Conda (recommended)
conda create -n creative_pathways python=3.11 -y
conda activate creative_pathways

# Install dependencies
pip install -r requirements.txt

# Seed database
python seed_data.py

# Optional: Add more artists
python expand_database.py

# Start server
uvicorn main:app --reload
```

Backend runs at: http://localhost:8000

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend runs at: http://localhost:5173

## 🎯 Usage

1. **Browse Artists**: Explore 50+ creators from various domains
2. **Filter by Domain**: Use dropdown to filter by Singer, Rapper, YouTuber, etc.
3. **View Timelines**: Click any artist to see their complete career journey
4. **Get Matched**: Click "Get Started" to find artists similar to you
5. **Generate Roadmap**: Create a personalized 12-month action plan

## 📊 Database

The database includes:
- **50+ Artists** across 13+ domains
- **200+ Career Events** with detailed timelines
- Domains: Singers, Rappers, YouTubers, DJs, Producers, Actors, Comedians, Podcasters, Gamers, Dancers, Entrepreneurs, Beauty Influencers, Educators

## 🌐 Deployment

### Vercel (Recommended)

1. Fork this repository
2. Import to Vercel
3. Configure environment variables:
   - `DATABASE_URL`: SQLite connection string
   - `BACKEND_CORS_ORIGINS`: Your frontend URL
4. Deploy!

## 📝 Environment Variables

Create `.env` in backend directory:

```env
DATABASE_URL=sqlite:///./creative_pathways.db
BACKEND_CORS_ORIGINS=["http://localhost:5173"]
DEBUG=True
```

## 🤝 Contributing

This is a capstone project. Feel free to fork and adapt for your own use!

## 📄 License

MIT License - feel free to use for educational purposes

## 👨‍💻 Author

Built as a capstone project demonstrating:
- Full-stack web development
- Database design and ORM
- RESTful API development
- Modern frontend frameworks
- Recommendation algorithms
- Data engineering

---

**Note**: This project uses SQLite for simplicity. For production at scale, consider PostgreSQL or similar.
