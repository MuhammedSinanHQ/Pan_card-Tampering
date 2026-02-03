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

## Heroku Deployment

### Prerequisites for Heroku

- Heroku account (sign up at https://heroku.com)
- Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
- Git installed

### Deployment Steps

**Step 1:** Login to Heroku
```bash
heroku login
```

**Step 2:** Create a new Heroku app
```bash
heroku create your-app-name
```
Or let Heroku generate a random name:
```bash
heroku create
```

**Step 3:** Verify your files are ready
Make sure you have these files in your repository:
- `app.py` - Flask application entry point
- `Procfile` - Tells Heroku how to run the app
- `requirements.txt` - Lists all Python dependencies
- `utils.py` - Utility functions for image processing

**Step 4:** Initialize git repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit for Heroku deployment"
```

**Step 5:** Deploy to Heroku
```bash
git push heroku main
```
If you're on master branch:
```bash
git push heroku master
```

**Step 6:** Open your deployed app
```bash
heroku open
```

**Step 7:** View logs (if needed)
```bash
heroku logs --tail
```

### Important Notes for Heroku Deployment

- The app uses `opencv-python-headless` which is optimized for server environments
- Gunicorn is used as the WSGI server (defined in Procfile)
- File uploads are temporarily stored and not persisted across dyno restarts
- For production use, consider using cloud storage (S3, Cloudinary) for file persistence

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
├── Procfile                 # Heroku process configuration
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

**Issue:** Heroku deployment fails
- Check Heroku logs: `heroku logs --tail`
- Verify Procfile exists and is correctly formatted
- Ensure all dependencies are in requirements.txt

## License

This project is for educational purposes.

## Credits

Made by Pianalytix
