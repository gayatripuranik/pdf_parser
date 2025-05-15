import streamlit as st
from langchain_community.llms import Ollama
import pytesseract as tess
from PIL import Image
import fitz
import io

st.title('QuickGist: PDF and Article AI Summarizer')
uploaded_file = st.file_uploader("UPLOAD PDF", type='pdf')

def pdf_to_images(pdf_data):
    pdf_document = fitz.open(stream=pdf_data, filetype="pdf")

    images = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        images.append(img)

    return images

def process_uploaded_file(uploaded_file):
    # Convert PDF to images
    images = pdf_to_images(uploaded_file.read())
    tess.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.5.0/bin/tesseract'
    text = ""
    for img in images:
        text += tess.image_to_string(img) + "\n"

    return text

#with open('qa_f.pkl', 'rb') as f:
    #qa = pickle .load(f)

if uploaded_file is not None:
    text = process_uploaded_file(uploaded_file)
    st.write("Uploaded file:", uploaded_file.name)

    # Create a passage for summarization
    passage = f"Here is a passage: {text}\nQuestion: summarize the article"

    # Invoke LLM to summarize the passage
    llm = Ollama(model="phi3")  # Ensure the model and parameters are set correctly
    result = llm.invoke(passage)  # Adjust if needed based on the library's API

    # Display assistant's message
    st.chat_message("assistant").write(f"{result}")


if uploaded_file is None:
    #text = process_uploaded_file(uploaded_file)
    #with st.container(height=300):
        #st.markdown(text)
    #st.write("enter article:", uploaded_file.name)
    messages = st.container(height=300)
    if prompt := st.chat_input("enter article"):
        messages.chat_message("user").write(prompt)
        #ans = qa(text,str(prompt))
        passage = f"Here is a passage: {prompt}\nQuestion: summarize the article"
        llm = Ollama(model="phi3")
        result = llm.invoke(passage)
        messages.chat_message("assistant").write(f"{result}")