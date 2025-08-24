📄 ATS Resume Expert

An AI-powered Applicant Tracking System (ATS) Resume Analyzer built with Streamlit and Google Gemini AI.
This tool helps job seekers optimize their resumes against job descriptions by providing:

✅ Resume Summary – Detailed analysis of key skills, strengths, and suitability.
✅ Skill Gap Suggestions – Actionable advice on missing skills, certifications, and improvements.
✅ ATS Match Score – A percentage match with key skills/keywords from the job description.

🚀 Features

Upload your resume (PDF format).

Paste or write the job description of your target role.

Get AI-powered analysis with Gemini 1.5 Flash.

Highlights ATS-relevant keywords and missing skills.

Helps make resumes more recruiter-friendly.

🛠️ Tech Stack

Python 🐍

Streamlit (frontend & backend)

Google Generative AI (Gemini API)

pdf2image + Pillow (for PDF parsing)

Base64 & I/O handling for document processing

📂 How to Run Locally
# Clone the repository
git clone https://github.com/your-username/ats-resume-expert.git  

cd ats-resume-expert  

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux

# Install dependencies
pip install -r requirements.txt  

# Add your Google API key in .env
GOOGLE_API_KEY=your_api_key_here  

# Run the app
streamlit run app.py


Open 👉 http://localhost:8501/


📌 Future Enhancements

Support for multi-page PDF resumes.
Multiple resume template scoring formats.
Export results in PDF/Word format.
Integration with LinkedIn / GitHub APIs.
