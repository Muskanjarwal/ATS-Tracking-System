from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

# configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    # Use a multimodal Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, pdf_content[0], prompt])
    
    # Safely extract text
    if hasattr(response, "text"):
        return response.text
    else:
        return response.candidates[0].content.parts[0].text

def input_pdf_setup(uploaded_file):
    # convert the pdf to image
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")


# streamlit app

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")

uploaded_files=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])

if uploaded_files is not None:
    st.write("PDF Uploaded Successfully")

submit1=st.button("Tell Me About The Resume")

submit2=st.button("How Can I Improve my Skills")

submit3=st.button("Percentage Match")

if submit1:
    if uploaded_files is not None:
        pdf_content = input_pdf_setup(uploaded_files)
        input_prompt1 = """
        You are an expert career assistant. 
        Analyze the candidate’s resume and provide a detailed summary of:
        - Key skills and experiences
        - Strengths
        - Role suitability based on the job description
        Write in a professional and ATS-friendly way.
        """
        response = get_gemini_response(input_text, pdf_content, input_prompt1)
        st.subheader("Resume Summary")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit2:
    if uploaded_files is not None:
        pdf_content = input_pdf_setup(uploaded_files)
        input_prompt2 = """
        You are an ATS and career expert. 
        Based on the job description and the candidate’s resume:
        - Highlight missing skills
        - Suggest improvements in technical & soft skills
        - Recommend certifications, projects, or experiences to add
        Keep it actionable and realistic.
        """
        response = get_gemini_response(input_text, pdf_content, input_prompt2)
        st.subheader("Skill Improvement Suggestions")
        st.write(response)
    else:
        st.write("Please upload the resume")
    

if submit3:
    if uploaded_files is not None:
        pdf_content = input_pdf_setup(uploaded_files)
        input_prompt3 = """
        You are an ATS (Applicant Tracking System).
        Compare the resume with the job description and provide:
        - A percentage match (0-100%)
        - Key matching keywords/skills
        - Missing important keywords
        """
        response = get_gemini_response(input_text, pdf_content, input_prompt3)
        st.subheader("ATS Score & Match Report")
        st.write(response)
    else:
        st.write("Please upload the resume")

