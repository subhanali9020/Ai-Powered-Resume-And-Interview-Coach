# Function define karna
def process_resume(raw_text):
    # Text clean karna
    cleaned_text = raw_text.strip().lower().replace("\n", " ")
    
    # Dictionary banana (Structured Data)
    # AI models backend par is tarah data handle karte hain
    resume_data = {
        "candidate_name": "Subhan Ali",
        "cleaned_content": cleaned_text,
        "word_count": len(cleaned_text.split()), # split() se words ki list banegi aur len() usko count karega
        "is_ready_for_ai": True
    }
    
    return resume_data

# Ek lamba raw resume text
dummy_resume = """
   Subhan Ali
  Mobile Developer | AI Enthusiast 
  
  Skills: Kotlin, Python, Machine Learning, Jetpack Compose  
"""

# Function call karna aur result variable mein save karna
final_result = process_resume(dummy_resume)

# Dictionaries se specific data nikalna
print("Name:", final_result["candidate_name"])
print("Total Words:", final_result["word_count"])
print("Status:", final_result["is_ready_for_ai"])
print("Data Payload:", final_result)
