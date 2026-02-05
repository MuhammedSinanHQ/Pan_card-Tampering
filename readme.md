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

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Quick Start - Deploy to Render

#### Method 1: Blueprint Deployment (Recommended)

1. Fork or clone this repository to your GitHub account
2. Sign up for a [Render account](https://render.com)
3. In the Render Dashboard, click **"New +"** → **"Blueprint"**
4. Connect your GitHub repository
5. Select this repository - Render will detect `render.yaml`
6. Click **"Apply"** to deploy

Your app will be live at: `https://your-app-name.onrender.com`

#### Method 2: Manual Setup

1. Sign up for a [Render account](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --timeout 60`
   - **Environment:** Python 3
5. Add environment variable: `SECRET_KEY` (generate a secure random string)
6. Click **"Create Web Service"**

### Important Notes for Render Deployment

- The app uses `opencv-python-headless` which is optimized for server environments
- Gunicorn is used as the WSGI server
- Free tier services spin down after 15 minutes of inactivity (30-60s cold start)
- File uploads are temporarily stored and not persisted across restarts
- For production use, consider using cloud storage (S3, Cloudinary) or Render Disks

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
├── render.yaml              # Render blueprint configuration
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
- Check Render logs in the Dashboard (Logs tab)
- Verify render.yaml or start command is correctly configured
- Ensure all dependencies are in requirements.txt

## License

This project is for educational purposes.

## Credits

Made by Pianalytix
