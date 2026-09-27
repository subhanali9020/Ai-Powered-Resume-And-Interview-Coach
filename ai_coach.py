import requests
import config 
import json

API_KEY = config.GEMINI_API_KEY

print("🧠 Phase 7: AI Coach is analyzing with Advanced Prompt Engineering...")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"
headers = {'Content-Type': 'application/json'}

# 🚀 PHASE 7: Advanced Prompt Engineering (Structured Output & ATS Focus)
prompt = """
You are an expert AI Career Coach and a strict ATS (Applicant Tracking System).
Analyze the candidate's resume against the target role of "AI Engineer".

Resume Data: 
Name: Subhan Ali. 
Skills: Kotlin, Jetpack Compose, Python, REST APIs. 
Experience: 2 years in Android App Development, exploring AI concepts.

Task: Provide an ATS evaluation.
CRITICAL: You MUST respond ONLY in valid JSON format. Do not add any markdown, greetings, or extra text. Use exactly this JSON schema:

{
  "ats_score": <number between 0 and 100>,
  "missing_keywords": ["keyword1", "keyword2", "keyword3"],
  "improvement_tips": ["tip1", "tip2"]
}
"""

payload = {"contents": [{"parts": [{"text": prompt}]}]}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    ai_response_text = result['candidates'][0]['content']['parts'][0]['text']
    
    # Defensive programming: Agar AI ghalti se ```json aur ``` laga de, toh usay hata do
    ai_response_text = ai_response_text.replace("```json\n", "").replace("```", "")
    
    # String ko asli Python Dictionary (JSON) mein convert karna
    parsed_data = json.loads(ai_response_text)
    
    print("\n✅ Python ne JSON ko successfully samajh liya!")
    print(f"🎯 ATS Score: {parsed_data['ats_score']}/100")
    print(f"🔍 Pehla Missing Keyword: {parsed_data['missing_keywords'][0]}")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)