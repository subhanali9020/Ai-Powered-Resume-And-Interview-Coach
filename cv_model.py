import cv2

def check_image_quality(image_path):
    print(f"🖼️ Checking profile picture: {image_path}...")
    
    # 1. Image read karna (Grayscale mein kyunke blur detection ke liye color zaroori nahi)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("❌ Error: Image file nahi mili. Kya file folder mein majood hai?")
        return

    # 2. Laplacian Variance (Smart CV trick to check blur)
    # Laplacian image mein "edges" (kinaray) dhoondta hai. 
    # Agar picture sharp hogi, toh variance high hoga. Agar dhundli hogi, toh variance low hoga.
    blur_score = cv2.Laplacian(img, cv2.CV_64F).var()
    
    print(f"📊 Image Sharpness Score: {blur_score:.2f}")
    
    # 3. Decision threshold (Aam taur par 100 se kam score blurry maana jata hai)
    if blur_score < 100:
        print("Verdict: Profile Picture is BLURRY ❌ (Please upload a clear photo)\n")
    else:
        print("Verdict: Profile Picture is CLEAR ✅ (Good to go!)\n")

# Isko test karne ke liye hum file call karte hain
check_image_quality("test_photo.jpg")