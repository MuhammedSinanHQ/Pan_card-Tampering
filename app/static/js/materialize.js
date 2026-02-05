// Minimal materialize.js for Pan Card Tampering app
console.log('Pan Card Tampering app loaded');

// Initialize file field functionality
document.addEventListener('DOMContentLoaded', function() {
    // Get all file-field containers
    var fileFields = document.querySelectorAll('.file-field.input-field');
    
    fileFields.forEach(function(fileField) {
        var btn = fileField.querySelector('.btn');
        var fileInput = fileField.querySelector('input[type="file"]');
        
        if (btn && fileInput) {
            // When the button is clicked, trigger the hidden file input
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                fileInput.click();
            });
        }
    });
});
