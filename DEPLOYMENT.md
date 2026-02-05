# Render Deployment Guide

This document provides step-by-step instructions for deploying the Pan Card Tampering Detection Flask app to Render.

## Prerequisites

Before you begin, ensure you have:

1. A Render account (sign up at https://render.com)
2. Git installed and configured
3. The repository hosted on GitHub, GitLab, or Bitbucket
4. Python 3.7 or higher

## Deployment Options

You can deploy this application to Render in two ways:

### Option 1: Using render.yaml Blueprint (Recommended)

The repository includes a `render.yaml` blueprint file that automates the deployment configuration.

### Option 2: Manual Setup via Render Dashboard

Follow the manual setup instructions below if you prefer to configure deployment settings through the Render web interface.

---

## Option 1: Deploy Using render.yaml Blueprint

### Step 1: Connect Your Repository

1. Log in to your Render account at https://dashboard.render.com
2. Click on "New +" and select "Blueprint"
3. Connect your GitHub, GitLab, or Bitbucket account if not already connected
4. Select the repository: `MuhammedSinanHQ/Pan_card-Tampering`
5. Render will automatically detect the `render.yaml` file

### Step 2: Configure Blueprint

1. Review the blueprint configuration:
   - **Service Name**: pan-card-tampering
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --timeout 60`
2. Render will auto-generate a `SECRET_KEY` environment variable
3. Click "Apply" to create the service

### Step 3: Monitor Deployment

1. Render will automatically:
   - Build your application
   - Install dependencies from requirements.txt
   - Start the application with gunicorn
2. Monitor the deployment logs in real-time
3. Once deployed, your app will be available at: `https://pan-card-tampering.onrender.com`

### Step 4: Verify Deployment

1. Navigate to your Render app URL
2. Upload a test image to verify functionality
3. Check that image processing works correctly

---

## Option 2: Manual Deployment via Render Dashboard

### Step 1: Create a New Web Service

1. Log in to Render at https://dashboard.render.com
2. Click "New +" and select "Web Service"
3. Connect your repository (GitHub, GitLab, or Bitbucket)
4. Select the repository: `MuhammedSinanHQ/Pan_card-Tampering`

### Step 2: Configure the Web Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `pan-card-tampering` (or your preferred name)
- **Region**: Choose your preferred region (e.g., Oregon, Frankfurt, Singapore)
- **Branch**: `main` (or your default branch)
- **Root Directory**: Leave empty (use repository root)

**Build & Deploy:**
- **Runtime**: `Python 3`
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  gunicorn app:app --timeout 60
  ```

**Instance Type:**
- **Free** tier is sufficient for testing
- **Starter** or higher for production use

### Step 3: Set Environment Variables

Add the following environment variable:

- **SECRET_KEY**: Generate a secure random string for production
  - Click "Add Environment Variable"
  - Key: `SECRET_KEY`
  - Value: Your secure random string (or click "Generate" if available)

Example of generating a secure key:
```python
import secrets
secrets.token_hex(32)
```

### Step 4: Deploy

1. Click "Create Web Service"
2. Render will:
   - Clone your repository
   - Install dependencies
   - Start your application with gunicorn
3. Monitor the deployment in the logs section

### Step 5: Access Your Application

Once deployment is complete:
1. Your app will be available at: `https://your-app-name.onrender.com`
2. The URL is shown in your Render dashboard

---

## Post-Deployment

### View Application Logs

1. Go to your Render dashboard
2. Select your web service
3. Click on the "Logs" tab to view real-time logs

### Environment Variables

To update environment variables:
1. Go to your service in Render dashboard
2. Navigate to "Environment" tab
3. Add or modify variables
4. Click "Save Changes" (will trigger automatic redeploy)

### Manual Deploy

To manually trigger a deployment:
1. Go to your service dashboard
2. Click "Manual Deploy"
3. Select "Clear build cache & deploy" if needed

### Suspend/Resume Service

For free tier services:
- Services automatically sleep after 15 minutes of inactivity
- First request after sleep may take 30-60 seconds
- To prevent sleep, upgrade to a paid plan

---

## Configuration

### Required Files

Ensure the following files are present:

**requirements.txt:**
```
flask
imutils
opencv-python-headless
Pillow
scikit-image
gunicorn
```

**app.py** (entry point):
```python
from app import app

if __name__ == "__main__":
    app.run()
```

**render.yaml** (optional, for blueprint deployment):
```yaml
services:
  - type: web
    name: pan-card-tampering
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app --timeout 60
    envVars:
      - key: SECRET_KEY
        generateValue: true
```

---

## Troubleshooting

### Application Crashes

1. **Check logs**: View logs in Render dashboard
2. **Verify dependencies**: Ensure all packages are in requirements.txt
3. **Check Python version**: Render uses Python 3.7+ by default
4. **Verify start command**: Ensure gunicorn command is correct

### Build Failures

1. **Missing dependencies**: Add missing packages to requirements.txt
2. **OpenCV issues**: Using `opencv-python-headless` (optimized for servers)
3. **Memory issues during build**: Consider upgrading instance type

### Runtime Errors

1. **Import errors**: Verify all dependencies are installed
2. **File path issues**: Use absolute paths from basedir (see config.py)
3. **Environment variables**: Check SECRET_KEY is set

### File Upload Issues

Render's filesystem is ephemeral:
- Uploaded files persist during runtime
- Files are cleared on each deployment
- For persistent storage, consider:
  - AWS S3
  - Cloudinary
  - Render Disks (for persistent volumes)

---

## Testing the Deployed Application

1. Navigate to your Render app URL
2. Upload the sample tampered image from `sample_data/image/tampered.png`
3. Verify the similarity percentage is displayed (should be around 31-32%)
4. Upload the original image and verify 100% similarity

---

## Updating Your Application

Automatic deployment on Git push:
1. Push changes to your main branch
2. Render automatically detects changes
3. Triggers build and deployment
4. Monitor progress in logs

Manual deployment:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

---

## Useful Render Features

### Custom Domains

1. Go to service settings
2. Click "Custom Domain"
3. Add your domain and configure DNS

### Health Checks

Render automatically performs health checks:
- Path: `/` (root path)
- Interval: Every 30 seconds
- Configure custom health check paths if needed

### Auto-Deploy

- Enabled by default for the main branch
- Disable in service settings if you prefer manual deploys

### Environment Groups

Create reusable environment variable groups:
1. Go to Dashboard
2. Click "Environment Groups"
3. Create a group and add variables
4. Link to multiple services

---

## Performance Optimization

### Free Tier Limitations

- Service sleeps after 15 minutes of inactivity
- 750 hours/month of service time
- Slower response times after sleep

### Paid Tier Benefits

- Always-on services (no sleep)
- Faster instances
- More memory and CPU
- Priority support

### Caching

Consider implementing caching for:
- Processed images
- Repeated comparisons
- Static assets

---

## Security Best Practices

1. **Environment Variables**: Never commit sensitive data
2. **SECRET_KEY**: Use a strong, unique secret key
3. **HTTPS**: Render provides SSL/TLS automatically
4. **Dependencies**: Keep packages updated for security patches
5. **Rate Limiting**: Consider adding rate limiting for production
6. **File Validation**: Validate uploaded file types and sizes

---

## Additional Resources

- Render Documentation: https://render.com/docs
- Python on Render: https://render.com/docs/deploy-flask
- Render Status Page: https://status.render.com
- Community Forum: https://community.render.com

---

## Support

For issues or questions:
1. Check Render logs first
2. Review Render documentation
3. Visit Render community forum
4. Check the project's GitHub issues
5. Contact the project maintainers

---

## Cost Information

**Free Tier:**
- 750 hours/month
- Services sleep after 15 minutes of inactivity
- Sufficient for development and testing

**Starter Plan** ($7/month per service):
- Always-on service
- Faster instances
- No sleep time

**Standard Plan** ($25/month per service):
- More CPU and memory
- Better performance
- Priority support

For current pricing, visit: https://render.com/pricing
