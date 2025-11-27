# Vercel Deployment Guide

## 🚀 Quick Deploy to Vercel

### Step 1: Import Project to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Import from GitHub: `abhibade619/creativepathway`
4. Click "Import"

### Step 2: Configure Build Settings

Vercel should auto-detect the configuration from `vercel.json`, but verify:

**Framework Preset**: Other

**Root Directory**: `./`

**Build Command**: 
```bash
cd frontend && npm install && npm run build
```

**Output Directory**: `frontend/dist`

### Step 3: Environment Variables

Add these environment variables in Vercel dashboard:

```
DATABASE_URL=sqlite:///./creative_pathways.db
BACKEND_CORS_ORIGINS=["https://creativepathway.vercel.app"]
DEBUG=False
```

**Note**: Replace `creativepathway.vercel.app` with your actual Vercel domain.

### Step 4: Deploy!

Click "Deploy" and wait for the build to complete.

## 📝 Post-Deployment

### Initialize Database

After first deployment, you need to seed the database:

1. Go to Vercel Dashboard → Your Project → Settings → Functions
2. Or use Vercel CLI:

```bash
vercel env pull
cd backend
python seed_data.py
python expand_database.py  # Optional: Add 40+ more artists
```

### Update CORS

Once deployed, update the backend `.env` or Vercel environment variables with your actual domain:

```
BACKEND_CORS_ORIGINS=["https://your-actual-domain.vercel.app"]
```

## 🔧 Troubleshooting

### Database Issues

If you get database errors:
- Vercel's serverless functions are stateless
- Consider using Vercel Postgres or another hosted database for production
- For demo purposes, SQLite works but data won't persist between deployments

### CORS Errors

Make sure:
1. `BACKEND_CORS_ORIGINS` includes your Vercel domain
2. Frontend API calls use relative URLs (`/api/...`) not absolute URLs

### Build Errors

Common fixes:
- Ensure `package.json` has correct build script
- Check that all dependencies are in `requirements.txt` and `package.json`
- Verify Python version compatibility (3.8+)

## 🎯 Alternative: Deploy Backend Separately

For better performance, consider:

1. **Backend**: Deploy to Railway, Render, or Heroku
2. **Frontend**: Deploy to Vercel
3. **Database**: Use PostgreSQL on Railway or Supabase

Update frontend `vite.config.js` proxy to point to your backend URL.

## 📊 Monitoring

After deployment:
- Check Vercel Analytics for traffic
- Monitor function logs in Vercel dashboard
- Test all features: browsing, filtering, matching, roadmap generation

## 🔄 Continuous Deployment

Every push to `main` branch will automatically deploy to Vercel!

```bash
git add .
git commit -m "Update features"
git push origin main
```

Vercel will automatically rebuild and redeploy.

---

**Your project is now live!** 🎉

Share with your teammates: `https://your-project.vercel.app`
