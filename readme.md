# Pan Card Tampering Detection

A Flask web application to detect tampering in PAN card images using Structural Similarity Index (SSIM) and OpenCV.

## Features

- Upload PAN card images for verification
- Compare uploaded image with original PAN card
- Calculate SSIM score to detect tampering
- Highlight differences with contour detection
- Simple and intuitive web interface

## Local Development

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

**Step 1:** Clone the repository
```bash
git clone <repository-url>
cd Pan_card-Tampering
```

**Step 2:** Create a virtual environment (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**Step 3:** Install dependencies
```bash
pip install -r requirements.txt
```

**Step 4:** Run the application
```bash
python app.py
```

**Step 5:** Open your browser and navigate to:
```
http://localhost:5000
```

**Step 6:** Test the application using sample images from `sample_data/image/` directory

## Render Deployment

### Prerequisites for Render

- Render account (sign up at https://render.com)
- Git repository hosted on GitHub, GitLab, or Bitbucket

### Quick Deploy with Blueprint

This repository includes a `render.yaml` blueprint for easy deployment:

**Step 1:** Push the code to your Git repository

**Step 2:** Log in to Render Dashboard
```
https://dashboard.render.com
```

**Step 3:** Create a new Blueprint
- Click "New +" and select "Blueprint"
- Connect your repository
- Render will automatically detect `render.yaml`
- Click "Apply" to deploy

**Step 4:** Your app will be deployed at:
```
https://your-app-name.onrender.com
```

### Manual Render Deployment

If you prefer manual configuration:

**Step 1:** Create a new Web Service in Render Dashboard

**Step 2:** Configure the service:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app --timeout 60`
- **Environment**: Python 3

**Step 3:** Add environment variable:
- **SECRET_KEY**: Generate a secure random string

**Step 4:** Deploy and access your app

### Important Notes for Render Deployment

- The app uses `opencv-python-headless` which is optimized for server environments
- Gunicorn is used as the WSGI server
- File uploads are temporarily stored and not persisted across deployments
- For production use, consider using cloud storage (S3, Cloudinary) for file persistence
- Free tier services sleep after 15 minutes of inactivity
- See `DEPLOYMENT.md` for detailed deployment instructions

## Project Structure

```
Pan_card-Tampering/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── views.py             # Route handlers
│   ├── templates/
│   │   └── index.html       # Main HTML template
│   └── static/
│       ├── css/             # Stylesheets
│       ├── js/              # JavaScript files
│       ├── uploads/         # Temporary uploaded images
│       ├── original/        # Original PAN card images
│       └── generated/       # Generated comparison images
├── sample_data/
│   └── image/               # Sample PAN card images for testing
├── app.py                   # Application entry point
├── utils.py                 # Image processing utilities
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment blueprint
├── DEPLOYMENT.md            # Detailed deployment guide
├── .gitignore              # Git ignore rules
└── readme.md               # This file
```

## How It Works

1. User uploads a PAN card image through the web interface
2. The image is resized to standard dimensions (250x160)
3. The uploaded image is compared with the original PAN card
4. SSIM (Structural Similarity Index) is calculated between the images
5. Differences are highlighted using contour detection
6. Results showing similarity percentage are displayed to the user

## Technologies Used

- **Flask** - Web framework
- **OpenCV** - Image processing
- **scikit-image** - SSIM calculation
- **Pillow** - Image manipulation
- **imutils** - Image utilities
- **Gunicorn** - WSGI HTTP Server

## Testing

Use the sample images provided in `sample_data/image/`:
- `original.png` - Original PAN card
- `tampered.png` - Tampered version for testing

## Security Considerations

- Don't commit sensitive PAN card images to the repository
- Use environment variables for sensitive configuration
- The SECRET_KEY should be changed in production
- Consider adding rate limiting for production deployment

## Troubleshooting

**Issue:** Application doesn't start
- Check if all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.7+)

**Issue:** Image upload fails
- Ensure the static directories exist
- Check file permissions
- Verify file size is reasonable (< 10MB)

**Issue:** Render deployment fails
- Check Render logs in the dashboard
- Verify all dependencies are in requirements.txt
- Ensure start command is correct: `gunicorn app:app --timeout 60`

## License

This project is for educational purposes.

## Credits

Made by Pianalytix
