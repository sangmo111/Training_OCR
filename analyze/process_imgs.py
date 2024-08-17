#Use a Python script to run Tesseract on all your images and save the outputs:

import os
import subprocess

# Directory containing images
image_dir = '/Users/jinpa/Desktop/images'
# Directory to save OCR outputs
output_dir = '/Users/jinpa/Desktop/outputs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each image in the directory
for image_file in os.listdir(image_dir):
    if image_file.endswith('.png') or image_file.endswith('.jpg'):
        image_path = os.path.join(image_dir, image_file)
        output_path = os.path.join(output_dir, os.path.splitext(image_file)[0])

        # Run Tesseract OCR
        subprocess.run([
            'tesseract', image_path, output_path,
            '--oem', '1', '--psm', '3', '-l', 'Noto_Serif_Tibetan'
        ])
