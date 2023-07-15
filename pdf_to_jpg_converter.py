import os
from pdf2image import convert_from_path

# Specify the PDF file path
pdf_path = '/path/to/your/pdf/file.pdf'

first_page = #
last_page = #

# Specify the output directory to save the JPG images
output_dir = '/path/to/output/directory/'

# Convert PDF pages to JPG images
images = convert_from_path(pdf_path, dpi=300, first_page = first_page, last_page = last_page)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save the JPG images to the output directory
for i, image in enumerate(images):
    image.save(os.path.join(output_dir, f'page_{i+1}.jpg'), 'JPEG')
