# PDF Summarizer with OpenAI

A simple tool that allows users to select a PDF, OCR its content, summarize it using OpenAI's GPT model, and save the summarized content as text, Word, and PDF.

## Requirements
- OpenAI Python API
- PyPDF2 for PDF reading
- pytesseract for OCR
- PIL for image processing
- python-docx for Word document creation
- fpdf for PDF creation
- tkinter for GUI

## Setup
1. Install required libraries:

2. Make sure you have Tesseract installed: https://github.com/tesseract-ocr/tesseract/wiki

3. Replace `YOUR_OPENAI_API_KEY` in the code with your actual OpenAI API key.

## Usage
Run the script. You'll be prompted to:
1. Choose a PDF file for OCR.
2. Choose a folder to save the summarized content.

The summarized content will be saved in three formats: .txt, .docx, and .pdf.
