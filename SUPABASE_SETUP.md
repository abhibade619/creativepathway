# Supabase Setup Instructions

## 🎯 What You Need to Do

You need to get the **PostgreSQL connection string** from Supabase.

### Step 1: Get Database Password

1. Go to your Supabase project: https://dvfltcfyujnrxeitosxd.supabase.co
2. Click **Settings** (gear icon) → **Database**
3. Scroll to **Connection String** section
4. Select **URI** tab
5. Copy the connection string (it will look like):
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.dvfltcfyujnrxeitosxd.supabase.co:5432/postgres
   ```
6. Replace `[YOUR-PASSWORD]` with your actual database password

### Step 2: Update Vercel Environment Variables

Go to Vercel → Your Project → Settings → Environment Variables

**Update DATABASE_URL:**
- Name: `DATABASE_URL`
- Value: `postgresql://postgres:[YOUR-PASSWORD]@db.dvfltcfyujnrxeitosxd.supabase.co:5432/postgres`
- Replace `[YOUR-PASSWORD]` with your actual password

**Keep these the same:**
- `BACKEND_CORS_ORIGINS`: `["https://your-vercel-url.vercel.app"]`
- `DEBUG`: `False`

### Step 3: Redeploy on Vercel

After updating the environment variable, click "Redeploy" in Vercel.

The app will:
1. Connect to Supabase PostgreSQL
2. Create tables automatically
3. Seed with 5 artists on first run
4. Data will persist across deployments! 🎉

---

## 🔑 Finding Your Database Password

If you don't remember your database password:

1. Go to Supabase Dashboard
2. Settings → Database
3. Click "Reset Database Password"
4. Set a new password
5. Use that in the connection string

---

## ✅ Benefits of Supabase

- ✅ **Persistent Data** - Survives deployments
- ✅ **PostgreSQL** - Production-ready database
- ✅ **Free Tier** - 500MB database, 2GB bandwidth
- ✅ **Automatic Backups**
- ✅ **Real-time subscriptions** (if you want to add that later)

---

## 📝 Connection String Format

```
postgresql://postgres:[PASSWORD]@db.dvfltcfyujnrxeitosxd.supabase.co:5432/postgres
```

Replace `[PASSWORD]` with your actual database password from Supabase.
