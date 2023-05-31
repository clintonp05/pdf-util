import PyPDF2
import os

# Directory path containing the PDF files
pdf_directory = './output/'

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
output_file = './merged/merged.pdf'

# Write the merged PDF to the output file
with open(output_file, 'wb') as file:
    pdf_merger.write(file)

pdf_merger.close()
print(f'{len(pdf_files)} PDF files merged into {output_file}.')
