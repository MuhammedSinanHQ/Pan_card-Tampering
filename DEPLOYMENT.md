# Heroku Deployment Guide

This document provides step-by-step instructions for deploying the Pan Card Tampering Detection Flask app to Heroku.

## Prerequisites

Before you begin, ensure you have:

1. A Heroku account (sign up at https://signup.heroku.com)
2. Heroku CLI installed on your machine
3. Git installed and configured
4. The repository cloned to your local machine

## Installation

### 1. Install Heroku CLI

**For macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**For Ubuntu/Debian:**
```bash
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

**For Windows:**
Download and install from: https://devcenter.heroku.com/articles/heroku-cli

### 2. Verify Installation

```bash
heroku --version
```

## Deployment Steps

### Step 1: Login to Heroku

```bash
heroku login
```

This will open a browser window where you can log in to your Heroku account.

### Step 2: Create a New Heroku Application

From the root directory of your project, run:

```bash
heroku create your-app-name
```

Or let Heroku generate a random name:

```bash
heroku create
```

This command will:
- Create a new Heroku app
- Add a git remote named "heroku" to your repository

### Step 3: Verify Your Configuration Files

Ensure the following files are present and correctly configured:

**Procfile:**
```
web: gunicorn app:app --timeout 60
```

**requirements.txt:**
```
flask
imutils
opencv-python-headless
Pillow
scikit-image
gunicorn
```

**app.py:**
```python
from app import app

if __name__ == "__main__":
    app.run()
```

### Step 4: Add and Commit Your Changes

If you've made any local changes:

```bash
git add .
git commit -m "Prepare for Heroku deployment"
```

### Step 5: Deploy to Heroku

Push your code to Heroku:

```bash
git push heroku main
```

If your default branch is `master`:

```bash
git push heroku master
```

### Step 6: Scale Your Application

Ensure at least one web dyno is running:

```bash
heroku ps:scale web=1
```

### Step 7: Open Your Application

```bash
heroku open
```

This will open your deployed application in your default web browser.

## Post-Deployment

### View Application Logs

To view real-time logs:

```bash
heroku logs --tail
```

To view the last 100 log lines:

```bash
heroku logs -n 100
```

### Check Dyno Status

```bash
heroku ps
```

### Restart Your Application

If needed, restart your application:

```bash
heroku restart
```

## Configuration

### Set Environment Variables

To set the SECRET_KEY for production:

```bash
heroku config:set SECRET_KEY=your-secret-key-here
```

To view all environment variables:

```bash
heroku config
```

## Troubleshooting

### Application Crashes

1. Check logs for error messages:
   ```bash
   heroku logs --tail
   ```

2. Ensure all dependencies are in requirements.txt

3. Verify the Procfile is correctly formatted

### Build Failures

1. Check that requirements.txt has all necessary packages
2. Ensure Python version compatibility (Heroku uses Python 3.x by default)
3. Check for typos in package names

### Memory Issues

If you encounter memory issues:

1. Consider upgrading your dyno type:
   ```bash
   heroku ps:resize web=standard-1x
   ```

### File Upload Issues

Remember that Heroku's ephemeral filesystem means uploaded files are not persisted across dyno restarts. For production:

1. Consider using AWS S3 or Cloudinary for persistent storage
2. Add appropriate error handling for missing files

## Testing the Deployed Application

1. Navigate to your Heroku app URL
2. Upload the sample tampered image from `sample_data/image/tampered.png`
3. Verify the similarity percentage is displayed (should be around 31-32%)
4. Upload the original image and verify 100% similarity

## Updating Your Application

To deploy updates:

```bash
git add .
git commit -m "Your update message"
git push heroku main
```

## Useful Commands

```bash
# View app information
heroku info

# Access bash on Heroku dyno
heroku run bash

# View configuration
heroku config

# View releases
heroku releases

# Rollback to previous release
heroku rollback

# View add-ons
heroku addons
```

## Cost Optimization

- Free tier dyno sleeps after 30 minutes of inactivity
- Free tier includes 550-1000 dyno hours per month
- For production apps, consider upgrading to Hobby or Standard dynos

## Security Best Practices

1. Never commit sensitive data to the repository
2. Use environment variables for secrets
3. Keep dependencies updated
4. Enable SSL (Heroku provides this automatically)
5. Consider adding rate limiting for production

## Additional Resources

- Heroku Dev Center: https://devcenter.heroku.com
- Python on Heroku: https://devcenter.heroku.com/categories/python-support
- Heroku CLI Commands: https://devcenter.heroku.com/articles/heroku-cli-commands

## Support

For issues or questions:
1. Check Heroku logs first
2. Review Heroku documentation
3. Check the project's GitHub issues
4. Contact the project maintainers
