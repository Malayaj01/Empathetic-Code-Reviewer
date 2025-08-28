import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
	model = genai.GenerativeModel("models/gemini-2.0-flash")
	response = model.generate_content("Say hello!")
	print("Gemini API response:", response.text)
except Exception as e:
	print("Error:", e)
