import tkinter as tk
from tkinter import filedialog
import PyPDF2
from pytesseract import image_to_string
from PIL import Image
from docx import Document
from fpdf import FPDF
import openai

# OpenAI API Key Initialization
openai.api_key = "YOUR_OPENAI_API_KEY"

def split_content_into_chunks(content, max_chunk_size=1500):
    words = content.split(" ")
    chunks = []

    current_chunk = ""
    for word in words:
        if len(current_chunk + " " + word) <= max_chunk_size:
            current_chunk += " " + word
        else:
            chunks.append(current_chunk)
            current_chunk = word
    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def summarize_with_openai(content_chunk):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Summarize the following content:\n{content_chunk}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

# File Picker for the PDF
root = tk.Tk()
root.withdraw()
pdf_file_path = filedialog.askopenfilename(title="Select a PDF to OCR", filetypes=[("PDF files", "*.pdf")])
if not pdf_file_path:
    print("No file chosen. Exiting...")
    exit()

# OCR the PDF
content = ""
pdf_reader = PyPDF2.PdfReader(open(pdf_file_path, 'rb'))  # Fixed this line
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    content += page.extract_text()
    if not content.strip():
        content += image_to_string(Image.open(pdf_file_path))

# Summarize using OpenAI with chunk handling
chunks = split_content_into_chunks(content)
summary_chunks = [summarize_with_openai(chunk) for chunk in chunks]
summary = " ".join(summary_chunks)

# Folder picker
folder_path = filedialog.askdirectory(title="Select a folder to save the summary")
if not folder_path:
    print("No folder chosen. Exiting...")
    exit()

# Save as Text
with open(f"{folder_path}/summary.txt", "w") as text_file:
    text_file.write(summary)

# Save as Word (.docx)
doc = Document()
doc.add_paragraph(summary)
doc.save(f"{folder_path}/summary.docx")

# Save as PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, summary)
pdf.output(f"{folder_path}/summary.pdf")

print("Summary saved successfully!")
