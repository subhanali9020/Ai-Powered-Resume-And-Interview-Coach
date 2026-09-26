import pandas as pd
import numpy as np # NumPy numbers aur math ke liye sabse fast library hai

# Hamara purana resume data
data = {
    "Candidate Name": ["Subhan Ali", "Ali Raza", "Usman Khan"],
    "Skills": ["Kotlin, Python, AI", "Java, Android", "Python, Machine Learning"],
    "Experience (Years)": [2, 4, 1]
}
df = pd.DataFrame(data)

# 1. Data ko CSV file (Excel format) mein SAVE karna
df.to_csv("resumes_database.csv", index=False)
print("✅ Data successfully CSV mein save ho gaya!\n")

# 2. CSV file ko wapis READ karna (Smart Work)
saved_df = pd.read_csv("resumes_database.csv")
print("--- Data Loaded from CSV ---")
print(saved_df)
print("\n")

# 3. NumPy/Pandas ka magic (Aggregation): Average experience nikalna
avg_exp = np.mean(saved_df['Experience (Years)'])
print(f"📊 Candidates ka Average Experience: {avg_exp} years")