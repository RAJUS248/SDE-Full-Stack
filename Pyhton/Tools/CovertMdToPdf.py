import os
import markdown
import pdfkit
from PyPDF2 import PdfMerger

# Folder containing the .md files
md_folder = r'C:\md-notes'
output_pdf = os.path.join(md_folder, 'notes.pdf')

# Keywords to help order chapters
priority_keywords = [
    'overview', 'industry', 'computer', 'os', 'coding', 'variables', 'data-type',
    'conditional', 'if', 'loop', 'function', 'debug', 'oops', 'class',
    'recursion', 'ds', 'data-structure', 'complexity', 'time', 'others'
]

# Function to sort based on keywords
def sort_key(filename):
    name = filename.lower()
    for index, keyword in enumerate(priority_keywords):
        if keyword in name:
            return index
    return len(priority_keywords) + 1  # Put unknown topics at the end

# Get all .md files
md_files = [f for f in os.listdir(md_folder) if f.endswith('.md')]
md_files.sort(key=sort_key)

# Temp folder to hold intermediate PDFs
temp_pdf_paths = []

print(f"Found {len(md_files)} markdown files. Starting conversion...\n")

for md_file in md_files:
    file_path = os.path.join(md_folder, md_file)
    base_name = os.path.splitext(md_file)[0]
    temp_pdf = os.path.join(md_folder, base_name + '.pdf')

    # Read markdown content
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Save as PDF
    pdfkit.from_string(html_content, temp_pdf)
    temp_pdf_paths.append(temp_pdf)

    print(f"✔ Converted: {md_file} ➜ {base_name}.pdf")

# Merge all PDFs
print("\nMerging all PDFs into one file...")
merger = PdfMerger()
for pdf in temp_pdf_paths:
    merger.append(pdf)

merger.write(output_pdf)
merger.close()

print(f"\n✅ Final PDF created at: {output_pdf}")

# Optional: Clean up intermediate PDFs
for pdf in temp_pdf_paths:
    os.remove(pdf)
print("🧹 Cleaned up temporary PDF files.")
