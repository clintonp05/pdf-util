import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import fitz
import os


dirname = os.path.dirname(__file__)

# def createTestPDF():
#     # Directory path to store the generated PDF files
#     output_directory = '../../assets/output/'

#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Generate 50 PDF files with 4 pages each
#     for i in range(50):
#         # Create a new PDF file
#         output_file = os.path.join(output_directory, f'file0{i+1}.pdf')
#         pdf = FPDF()

#         # Generate 4 pages for the PDF file
#         for page_num in range(4):
#             pdf.add_page()
#             pdf.set_font("Arial", size=12)
#             pdf.cell(200, 10, txt=f"This is page {page_num+1} of file{i+1}.pdf", ln=True)

#         # Write the PDF file to the output directory
#         pdf.output(output_file)

#     print("PDF files generated successfully.")

def mergePDF():
    
    # Directory path containing the PDF files
    pdf_directory = os.path.join(dirname, '../../assets/output/')

    # List to store PDF file paths
    pdf_files = []

    # Get the paths of all PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_files.append(os.path.join(pdf_directory, filename))

    # Sort the PDF files alphabetically (optional)
    pdf_files.sort()

    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Merge the PDF files
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            pdf_merger.append(file)

    # Output file path for the merged PDF
    output_file = os.path.join(dirname, '../../assets/merged/merged.pdf')

    #not deleting by if file exists to skip avoid caching issues by os to have more realtime file info
    #file exists works by metadata file which is provided by os on cachings
    try:
        if(os.path.exists(output_file)):
            os.remove(output_file)
    except OSError as error:
        print(error)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as file:
        pdf_merger.write(file)

    pdf_merger.close()
    print(f'{len(pdf_files)} PDF files merged into {output_file}.')
    return output_file

def imposeImg():
    # Path to the input PDF file
    input_file = '../../assets/merged/merged.pdf'

    # Path to the image file
    image_file = '../../assets/signature.jpg'

    # Path for the output PDF file
    output_file = '../../assets/signedOut/signedDoc.pdf'

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

def imposeImgV2():

    # Path to the input PDF file
    input_file = os.path.join(dirname, '../../assets/merged/merged.pdf')

    # Path to the image file
    image_file = os.path.join(dirname, '../../assets//signature.png')
    image_file_1 = os.path.join(dirname, '../../assets/signature-1.png')
    image_file_2 = os.path.join(dirname, '../../assets/signature.png')
    image_file_3 = os.path.join(dirname, '../../assets/signature-1.png')
    stamp = os.path.join(dirname, '../../assets/stamp.png')

    # Path for the output PDF file
    output_file = os.path.join(dirname, '../../assets/signedOut/signedDoc.pdf')

    #not deleting by if file exists to skip avoid caching issues by os to have more realtime file info
    #file exists works by metadata file which is provided by os on cachings
    try:
        if(os.path.exists(output_file)):
            os.remove(output_file)
    except OSError as error:
        print(error)    

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
    return output_file