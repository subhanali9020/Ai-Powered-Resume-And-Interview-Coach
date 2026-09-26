import torch
import torch.nn as nn

# 1. Neural Network Architecture Define Karna
class SimpleResumeNet(nn.Module):
    def __init__(self):
        super(SimpleResumeNet, self).__init__()
        
        # Hidden Layer: Input 3 features aayenge (Exp, Skills, Words), usko 5 'neurons' mein bhejenge
        self.layer1 = nn.Linear(3, 5)
        
        # Activation: ReLU (Agar value 0 se choti ho toh 0 kardo, warna waise hi aage jane do)
        self.relu = nn.ReLU()
        
        # Output Layer: 5 neurons se data aayega aur 1 final score (Quality) niklega
        self.layer2 = nn.Linear(5, 1)
        
        # Sigmoid: Final output ko 0.0 aur 1.0 ke darmiyan squeeze kar deta hai (Probability)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Data ka flow (Forward Pass)
        out = self.layer1(x)
        out = self.relu(out)
        out = self.layer2(out)
        out = self.sigmoid(out)
        return out

# 2. Model ko initialize karna
model = SimpleResumeNet()
print("🧠 Neural Network Structure:")
print(model)

# 3. Dummy Tensor (PyTorch mein Pandas array ya list ko 'Tensor' kehte hain)
# Resume: [3 Years Exp, 5 Skills, 250 Words]
dummy_resume_data = torch.tensor([[3.0, 5.0, 250.0]])

# 4. Forward Pass (Data ko network se guzarna)
# Kyunke abhi model train nahi hua (weights random hain), output ek random probability hogi
prediction = model(dummy_resume_data)

print("\n--- Prediction Output ---")
print(f"Raw Output (0 to 1): {prediction.item():.4f}")