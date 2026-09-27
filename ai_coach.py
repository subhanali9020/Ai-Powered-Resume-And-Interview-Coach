import requests
import config  # Yeh tumhari apni banayi hui file hai!

API_KEY = config.GEMINI_API_KEY

print("🤖 AI Resume Coach is analyzing the profile...")

# Model URL
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"
headers = {'Content-Type': 'application/json'}

# FYP Prompt
prompt = """
You are an expert AI Career Coach. 
Read this candidate's resume data and provide exactly 2 short, bullet-pointed, actionable tips to improve it for an AI Engineering role.
Keep the tone encouraging and professional.

Resume Data: 
Name: Subhan Ali. 
Skills: Kotlin, Jetpack Compose, Python, AI. 
Experience: 2 years in Android, transitioning to AI Engineer.
"""
payload = {"contents": [{"parts": [{"text": prompt}]}]}

# API Call
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    print("\n--- 📝 AI Coach Feedback ---")
    print(result['candidates'][0]['content']['parts'][0]['text'])
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)