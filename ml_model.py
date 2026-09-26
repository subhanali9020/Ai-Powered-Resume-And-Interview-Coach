from sklearn.tree import DecisionTreeClassifier

# 1. Training Data (AI ko sikhane ke liye past data)
# Hum 3 features de rahe hain: [Experience (Years), Total Skills, Word Count]
X_train = [
    [5, 8, 300],  # Senior: 5 yrs exp, 8 skills, 300 words
    [1, 2, 100],  # Beginner: 1 yr exp, 2 skills, 100 words
    [3, 5, 250],  # Mid-level: 3 yrs exp, 5 skills, 250 words
    [0, 1, 50]    # Poor: 0 exp, 1 skill, 50 words
]

# Labels: 1 matlab "Good", 0 matlab "Needs Improvement"
y_train = [1, 0, 1, 0]

# 2. Model Initialize aur Train karna (Smart Work!)
print("🤖 AI Model Training start...")
model = DecisionTreeClassifier() # Yeh humara classifier hai
model.fit(X_train, y_train)      # fit() ka matlab hai model data dekh kar khud pattern seekh raha hai
print("✅ Model Training Complete!\n")

# 3. Model ko Test Karna (Naya Resume)
# Farz karo user ne resume upload kiya jisme: 2 years exp, 4 skills, aur 180 words hain
new_resume_features = [[2, 4, 180]]
prediction = model.predict(new_resume_features)

print("--- AI Resume Quality Score ---")
print(f"Candidate Features: {new_resume_features[0]}")
if prediction[0] == 1:
    print("Verdict: Good Resume 👍")
else:
    print("Verdict: Needs Improvement 👎")