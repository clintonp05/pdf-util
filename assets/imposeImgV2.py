import fitz

# Path to the input PDF file
input_file = './merged/merged.pdf'

# Path to the image file
image_file = './signature.png'
image_file_1 = './signature-1.png'
image_file_2 = './signature.png'
image_file_3 = './signature-1.png'
stamp = './stamp.png'

# Path for the output PDF file
output_file = './signedOut/signedDoc.pdf'

# Open the input PDF file
pdf_doc = fitz.open(input_file)

# Load the image
image = fitz.open(image_file)
w = 150
h = 750

# Loop through each page of the PDF
for page_num in range(len(pdf_doc)):
    page = pdf_doc[page_num]
    image_rectangle = fitz.Rect(0, 0.85*h, w, h)
    image_rectangle_1 = fitz.Rect(0, 0.85*h, w+300, h)
    image_rectangle_2 = fitz.Rect(0, 0.85*h, w+600, h)
    image_rectangle_3 = fitz.Rect(0, 0.85*h, w+900, h)
    stamp_rectangle = fitz.Rect(0, 0.70*h, w+180, h-130)

    # Insert the image at the bottom of the page
    page.insert_image(image_rectangle,filename=image_file)
    page.insert_image(image_rectangle_1,filename=image_file_1)
    page.insert_image(image_rectangle_2,filename=image_file_2)
    page.insert_image(image_rectangle_3,filename=image_file_3)
    page.insert_image(stamp_rectangle,filename=stamp)

# Save the modified PDF to the output file
pdf_doc.save(output_file)
pdf_doc.close()

print(f'Image superimposed in each page of the PDF: {output_file}')
