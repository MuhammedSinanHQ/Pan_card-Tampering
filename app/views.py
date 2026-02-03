# Important imports
from app import app
from flask import request, render_template
import os
from PIL import Image
import utils
import config

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

# Create necessary directories
os.makedirs(app.config['INITIAL_FILE_UPLOADS'], exist_ok=True)
os.makedirs(app.config['EXISTING_FILE'], exist_ok=True)
os.makedirs(app.config['GENERATED_FILE'], exist_ok=True)

# Route to home page
@app.route('/', methods=['GET', 'POST'])
def index():

    # Execute if request is GET
    if request.method == 'GET':
        return render_template('index.html')

    # Execute if request is POST
    if request.method == 'POST':
        try:
            # Get uploaded image
            file_upload = request.files.get('file_upload')
            if not file_upload:
                return render_template('index.html', pred='Error: No file uploaded')

            filename = file_upload.filename

            # Define paths
            uploaded_image_path = os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg')
            original_image_path = os.path.join(app.config['EXISTING_FILE'], 'image.jpg')

            # Resize and save the uploaded image
            utils.resize_image(file_upload, uploaded_image_path, 250, 160)

            # Resize and save the original image to ensure both images match in size
            # Use original pan card from config
            original_source = app.config.get('ORIGINAL_PAN_CARD_PATH', 
                                            os.path.join('sample_data', 'image', 'original.png'))
            
            if os.path.exists(original_source):
                utils.resize_image(original_source, original_image_path, 250, 160)
            else:
                # If sample data doesn't exist, check if original already exists
                if not os.path.exists(original_image_path):
                    return render_template('index.html', 
                                         pred='Error: Original PAN card image not found')

            # Compare PAN cards using utils
            result = utils.compare_pan_cards(
                original_image_path,
                uploaded_image_path,
                app.config['GENERATED_FILE']
            )

            # Return result
            return render_template(
                'index.html',
                pred=str(result['percentage']) + ' % ' + 'similarity'
            )
        
        except ValueError as e:
            return render_template('index.html', pred=f'Error: {str(e)}')
        except Exception as e:
            app.logger.error(f'Unexpected error: {str(e)}')
            return render_template('index.html', pred='Error: Failed to process image')

# Main function
if __name__ == "__main__":
    app.run(debug=True)
