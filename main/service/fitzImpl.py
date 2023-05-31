import fitz

# Path to the input PDF file
input_file = './merged/merged.pdf'

# Path to the image file
image_file = './signature.png'

# Path for the output PDF file
output_file = './signedOut/signedDoc.pdf'

# Open the input PDF file
pdf_doc = fitz.open(input_file)

# Load the image
image = fitz.open(image_file)
image_page = image[0]

# Loop through each page of the PDF
for page_num in range(len(pdf_doc)):
    page = pdf_doc[page_num]
    rect = page.rect

    # Insert the image at the bottom of the page
    page.insert_image(rect, filename=image_file)

# Save the modified PDF to the output file
pdf_doc.save(output_file)
pdf_doc.close()