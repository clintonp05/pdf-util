from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Path to the input PDF file
input_file = './merged/merged.pdf'

# Path to the image file
image_file = './signature.jpg'

# Path for the output PDF file
output_file = './signedOut/signedDoc.pdf'

# Open the input PDF file
pdf_reader = PdfReader(input_file)
pdf_writer = PdfWriter()

# Load the image onto a canvas
image_width = 4 * inch  # Adjust the image width as needed
image_height = 2 * inch  # Adjust the image height as needed

# Loop through each page of the input PDF
for page_num in range(len(pdf_reader.pages)):
    # Create a new page with the same dimensions as the original page
    page = pdf_reader.pages[page_num]
    new_page = PdfWriter()
    new_page.add_page(page)

    # Get the canvas for the new page
    c = canvas.Canvas('temp.pdf', pagesize=(page.mediabox.width, page.mediabox.height))

    # Draw the existing page content on the new page
    c.showPage()
    c.save()

    # Load the new page into the PDF writer
    with open('temp.pdf', 'rb') as temp_file:
        new_page.add_page(PdfReader(temp_file).pages[0])

    # Load the image onto the new page
    with open(image_file, 'rb') as img_file:
        image = PdfReader(img_file).pages[0]
        image.scaleTo(image_width, image_height)
        image.x = (page.mediabox.getWidth() - image_width) / 2  # Adjust the x-coordinate as needed
        image.y = 0  # Adjust the y-coordinate to position the image at the bottom
        new_page.add_page(image)

    # Merge the modified page into the output PDF
    pdf_writer.add_page(new_page.pages[0])

# Write the modified PDF to the output file
with open(output_file, 'wb') as file:
    pdf_writer.write(file)

print(f'Image added at the bottom of the PDF: {output_file}')