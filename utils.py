"""
Utility module for Pan Card Tampering Detection
Contains reusable functions for image processing, comparison, and tampering detection
"""

import cv2
import imutils
from skimage.metrics import structural_similarity
from PIL import Image
import os


def resize_image(image_path, output_path, width=250, height=160):
    """
    Resize an image to specified dimensions
    
    Args:
        image_path: Path to input image
        output_path: Path to save resized image
        width: Target width (default: 250)
        height: Target height (default: 160)
    
    Returns:
        PIL Image object
    """
    image = Image.open(image_path).resize((width, height))
    image.save(output_path)
    return image


def convert_to_grayscale(image):
    """
    Convert BGR image to grayscale
    
    Args:
        image: OpenCV image in BGR format
    
    Returns:
        Grayscale image
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def calculate_ssim(image1, image2):
    """
    Calculate Structural Similarity Index (SSIM) between two images
    
    Args:
        image1: First grayscale image
        image2: Second grayscale image
    
    Returns:
        tuple: (score, diff) where score is SSIM value and diff is difference image
    """
    (score, diff) = structural_similarity(image1, image2, full=True)
    diff = (diff * 255).astype("uint8")
    return score, diff


def apply_threshold(image):
    """
    Apply binary threshold using Otsu's method
    
    Args:
        image: Input grayscale image
    
    Returns:
        Thresholded binary image
    """
    thresh = cv2.threshold(
        image,
        0,
        255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )[1]
    return thresh


def find_contours(image):
    """
    Find contours in a binary image
    
    Args:
        image: Binary image
    
    Returns:
        List of contours
    """
    cnts = cv2.findContours(
        image.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    cnts = imutils.grab_contours(cnts)
    return cnts


def draw_contours(image, contours):
    """
    Draw bounding rectangles around contours
    
    Args:
        image: Image to draw on (will be modified in place)
        contours: List of contours
    
    Returns:
        Modified image with rectangles drawn
    """
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )
    return image


def compare_pan_cards(original_path, uploaded_path, output_dir):
    """
    Compare two PAN card images and detect tampering
    
    Args:
        original_path: Path to original PAN card image
        uploaded_path: Path to uploaded PAN card image
        output_dir: Directory to save output images
    
    Returns:
        dict: Contains ssim_score, percentage, and paths to generated images
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read images
    original_image = cv2.imread(original_path)
    uploaded_image = cv2.imread(uploaded_path)
    
    # Convert to grayscale
    original_gray = convert_to_grayscale(original_image)
    uploaded_gray = convert_to_grayscale(uploaded_image)
    
    # Calculate SSIM
    score, diff = calculate_ssim(original_gray, uploaded_gray)
    
    # Apply threshold
    thresh = apply_threshold(diff)
    
    # Find contours
    cnts = find_contours(thresh)
    
    # Draw contours on both images
    original_marked = original_image.copy()
    uploaded_marked = uploaded_image.copy()
    
    draw_contours(original_marked, cnts)
    draw_contours(uploaded_marked, cnts)
    
    # Save output images
    output_paths = {
        'original': os.path.join(output_dir, 'image_original.jpg'),
        'uploaded': os.path.join(output_dir, 'image_uploaded.jpg'),
        'diff': os.path.join(output_dir, 'image_diff.jpg'),
        'thresh': os.path.join(output_dir, 'image_thresh.jpg')
    }
    
    cv2.imwrite(output_paths['original'], original_marked)
    cv2.imwrite(output_paths['uploaded'], uploaded_marked)
    cv2.imwrite(output_paths['diff'], diff)
    cv2.imwrite(output_paths['thresh'], thresh)
    
    return {
        'ssim_score': score,
        'percentage': round(score * 100, 2),
        'output_paths': output_paths
    }
