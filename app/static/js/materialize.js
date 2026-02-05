// Minimal materialize.js for Pan Card Tampering app
console.log('Pan Card Tampering app loaded');

// Initialize file field functionality
document.addEventListener('DOMContentLoaded', () => {
    // Get all file-field containers
    const fileFields = document.querySelectorAll('.file-field.input-field');
    
    fileFields.forEach((fileField) => {
        const btn = fileField.querySelector('.btn');
        const fileInput = fileField.querySelector('input[type="file"]');
        
        if (btn && fileInput) {
            // When the button is clicked, trigger the hidden file input
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                fileInput.click();
            });
        }
    });
});
