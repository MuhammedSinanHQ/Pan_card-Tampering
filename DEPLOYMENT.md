# Render Deployment Guide

This document provides step-by-step instructions for deploying the Pan Card Tampering Detection Flask app to Render.

## Prerequisites

Before you begin, ensure you have:

1. A Render account (sign up at https://render.com)
2. Git installed and configured
3. The repository available on GitHub (or GitLab/Bitbucket)
4. Access to push to the repository

## Deployment Methods

Render offers two deployment methods:
1. **Blueprint Deployment** (Recommended - Uses render.yaml)
2. **Manual Deployment** (Via Render Dashboard)

## Method 1: Blueprint Deployment (Recommended)

This method uses the `render.yaml` file to automatically configure your service.

### Step 1: Connect Your Repository to Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** button in the top right
3. Select **"Blueprint"**
4. Connect your GitHub account if not already connected
5. Select the repository: `MuhammedSinanHQ/Pan_card-Tampering`
6. Render will automatically detect the `render.yaml` file

### Step 2: Configure Environment Variables (Optional)

The blueprint automatically generates a `SECRET_KEY`. You can customize it:

1. In the blueprint setup, you'll see the detected services
2. Click on the service to expand environment variables
3. Modify `SECRET_KEY` if desired (or let Render auto-generate)

### Step 3: Deploy

1. Click **"Apply"** to create the service
2. Render will:
   - Install dependencies from `requirements.txt`
   - Start the application using gunicorn
   - Provide you with a live URL (e.g., `https://pan-card-tampering.onrender.com`)

### Step 4: Access Your Application

Once deployment completes (usually 2-5 minutes):
- Click the URL provided in the Render dashboard
- Your Flask application will be live!

## Method 2: Manual Deployment

If you prefer manual setup without the blueprint:

### Step 1: Create a New Web Service

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select the `MuhammedSinanHQ/Pan_card-Tampering` repository

### Step 2: Configure Build Settings

Fill in the following settings:

**Name:** `pan-card-tampering` (or your preferred name)

**Environment:** `Python 3`

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn app:app --timeout 60
```

**Instance Type:** `Free` (or select a paid tier for better performance)

### Step 3: Set Environment Variables

1. Scroll down to **Environment Variables** section
2. Add the following variable:
   - **Key:** `SECRET_KEY`
   - **Value:** Generate a secure random string (or use: `your-secret-key-here`)

To generate a secure secret key, you can use:
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Render will start building and deploying your application
3. Monitor the logs in real-time during deployment

### Step 5: Access Your Application

Once the build completes:
- Your app URL will be displayed at the top: `https://your-app-name.onrender.com`
- Click it to open your application

## Post-Deployment

### View Application Logs

To view application logs:

1. Go to your service in the Render Dashboard
2. Click on the **"Logs"** tab
3. View real-time logs or filter by date/time
4. Use the search functionality to find specific errors

### Check Service Status

In the Render Dashboard:
1. Navigate to your service
2. Check the status badge (should show "Live")
3. View deployment history
4. Monitor resource usage

### Redeploy Your Application

Render automatically redeploys when you push to your connected branch:

```bash
git add .
git commit -m "Update application"
git push origin main
```

Or manually trigger a deploy:
1. Go to your service in the Render Dashboard
2. Click **"Manual Deploy"** → **"Deploy latest commit"**

### Suspend/Resume Service

For free tier services that you're not actively using:
1. Go to service settings
2. Click **"Suspend Service"** to stop it
3. Click **"Resume Service"** when needed

## Configuration

### Environment Variables

To set environment variables in Render:

1. Go to your service in the Dashboard
2. Navigate to **"Environment"** tab
3. Click **"Add Environment Variable"**
4. Add key-value pairs

Example variables:
- `SECRET_KEY`: Your application secret key
- `PYTHON_VERSION`: `3.9.0` (or your preferred version)

To set SECRET_KEY via render.yaml, it's already configured to auto-generate.

### Custom Domain (Optional)

To add a custom domain:

1. Go to your service settings
2. Navigate to **"Custom Domain"** section
3. Click **"Add Custom Domain"**
4. Follow the instructions to configure DNS

## Troubleshooting

### Application Crashes or Won't Start

1. **Check logs for error messages:**
   - Go to Render Dashboard → Your Service → Logs tab
   - Look for Python errors or missing dependencies

2. **Verify all dependencies:**
   - Ensure `requirements.txt` includes all packages
   - Check for version conflicts

3. **Verify start command:**
   - Should be: `gunicorn app:app --timeout 60`
   - Check that `app.py` is in the root directory

### Build Failures

1. **Check requirements.txt:**
   - Ensure all package names are correct
   - Verify compatibility with Python version
   - Common packages needed:
     - flask
     - gunicorn
     - opencv-python-headless
     - Pillow
     - scikit-image
     - imutils

2. **Python version issues:**
   - Render uses Python 3.7+ by default
   - Specify version in environment variables if needed

3. **Memory issues during build:**
   - Upgrade to a paid instance type for more resources

### Image Upload Issues

1. **File upload fails:**
   - Check file size limits
   - Verify the static/uploads directory structure
   - Ensure proper file permissions

2. **Images not persisting:**
   - Render's ephemeral filesystem means uploaded files don't persist across deploys
   - For production, consider using:
     - AWS S3
     - Cloudinary
     - Render Disk storage (paid feature)

### Performance Issues

1. **Slow cold starts (Free tier):**
   - Free tier services spin down after 15 minutes of inactivity
   - First request after spin-down takes 30-60 seconds
   - Solution: Upgrade to paid tier for always-on instances

2. **Memory limits:**
   - Free tier: 512 MB RAM
   - If you hit limits, upgrade to Starter or higher tier

## Testing the Deployed Application

1. Navigate to your Render app URL (e.g., `https://pan-card-tampering.onrender.com`)
2. Upload the sample tampered image from `sample_data/image/tampered.png`
3. Verify the similarity percentage is displayed (should be around 31-32%)
4. Upload the original image and verify 100% similarity

**Note:** First request after inactivity (free tier) may take 30-60 seconds due to cold start.

## Updating Your Application

Render automatically deploys when you push to your connected Git branch:

```bash
git add .
git commit -m "Your update message"
git push origin main
```

You can also:
- Trigger manual deploys from the Dashboard
- Set up deploy hooks
- Configure auto-deploy settings

## Useful Features

### Dashboard Features
- **Metrics:** View CPU, memory, and bandwidth usage
- **Deploy Hooks:** Trigger deploys via webhook
- **Health Checks:** Configure custom health check endpoints
- **Shell Access:** Access shell via Dashboard for debugging

### Render CLI (Optional)

Install the Render CLI for command-line operations:

```bash
# Install via npm
npm install -g render-cli

# Login
render login

# List services
render services list

# View logs
render logs <service-id>
```

### Automatic Deploys

Render automatically deploys on:
- Push to connected branch (default: main)
- Pull request merges (configurable)

### Branch-based Deploys

You can create preview environments:
1. Enable "Preview Environments" in service settings
2. Each PR gets its own temporary URL
3. Automatically deleted when PR is closed

## Pricing

### Free Tier
- 750 hours/month of free usage
- Services spin down after 15 minutes of inactivity
- 512 MB RAM
- Shared CPU
- Perfect for development and testing

### Paid Tiers
- **Starter ($7/month):** Always-on, 512 MB RAM
- **Standard ($25/month):** 2 GB RAM, better CPU
- **Pro ($85/month):** 4 GB RAM, dedicated CPU

For production apps, consider at least the Starter tier to avoid cold starts.

## Security Best Practices

1. **Environment Variables:** Never commit secrets to the repository
2. **Auto-generated Secrets:** Use Render's secret generation feature
3. **HTTPS:** Render provides free SSL certificates automatically
4. **Dependencies:** Keep packages updated for security patches
5. **Rate Limiting:** Consider adding rate limiting for production (e.g., Flask-Limiter)
6. **DDoS Protection:** Available on paid tiers

## File Persistence

Render's filesystem is ephemeral by default:
- Files created during runtime are lost on redeploy/restart
- For persistent storage, use:
  - **Render Disks:** Persistent SSD storage (paid add-on)
  - **External Storage:** AWS S3, Cloudinary, Google Cloud Storage
  - **Databases:** Render PostgreSQL, Redis for data persistence

## Additional Resources

- **Render Documentation:** https://render.com/docs
- **Python on Render:** https://render.com/docs/deploy-flask
- **Render Community:** https://community.render.com
- **Blueprint Specification:** https://render.com/docs/blueprint-spec
- **Environment Variables:** https://render.com/docs/environment-variables

## Support

For issues or questions:
1. Check Render logs in the Dashboard
2. Review [Render documentation](https://render.com/docs)
3. Visit [Render Community](https://community.render.com)
4. Check the project's GitHub issues
5. Contact the project maintainers

## Migration from Heroku

If you're migrating from Heroku:

1. **Environment Variables:** Export from Heroku and import to Render
2. **Database:** Render offers PostgreSQL; migrate data as needed
3. **Add-ons:** Check Render equivalents for Heroku add-ons
4. **Custom Domains:** Update DNS records to point to Render
5. **Procfile:** Not needed (use render.yaml or configure start command in Dashboard)
