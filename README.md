PDF Summarizer
A Streamlit-based PDF summarization app that extracts text from uploaded PDF files using OCR and generates meaningful summaries using advanced LLM-based natural language processing.

Objective
Build a user-friendly application that allows users to upload PDF documents (including scanned/image-based ones), extract text using OCR, and produce concise summaries using Ollama Phi 3 for enhanced readability and understanding.

Technologies Used
Python – Core programming language

Streamlit – For building the web interface

PyMuPDF (fitz) – Converts PDF pages into images

pytesseract – OCR to extract text from images

Ollama Phi 3 – LLM used for generating intelligent summaries

PyCharm IDE – Development environment

Key Features
PDF Upload: Users can upload any PDF document via a clean Streamlit interface.

Image Conversion: Each PDF page is converted into an image using PyMuPDF.

OCR Text Extraction: Extracts readable text from images using pytesseract.

LLM Summarization: Summarizes the extracted text using Ollama Phi 3 for quick insights.

Interactive UI: Minimal and intuitive interface for ease of use.

How to Run

Clone the repository:

git clone https://github.com/gayatripuranik/pdf_parser.git
cd pdf_parser

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Notes
Make sure Tesseract OCR is installed and added to your system path.

Ollama should be running locally with Phi 3 installed.


