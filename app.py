from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def main():
    load_dotenv()
    st.set_page_config(page_title="PDFChat")
    st.header("Chat your PDF 💬")

     # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    # extract the text
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
    
      st.write(text)

if __name__ == '__main__' :
    main()
    