from flask import Flask, request
import cv2
import numpy as np
import joblib

app = Flask(__name__)

# Load the AI Brain
try:
    clf = joblib.load('pill_model.pkl')
    label_map = {0: "Red", 1: "Blue", 2: "White", "0": "Red", "1": "Blue", "2": "White"}
    print("AI Model Loaded Successfully!")
except Exception as e:
    print(f"Error: pill_model.pkl not found! {e}")

def get_color_prediction(hsv_values):
    h, s, v = hsv_values
    print(f"- ANALYZING - H: {int(h)} | S: {int(s)} | V: {int(v)}")

    # 1. TIGHTER BLUE RANGE
    # Blue is usually H: 90-130. We add a 'Saturation' check.
    # If S is low (below 50), it's probably just a white pill reflecting light.
    if 85 < h < 145 and s > 50: 
        return "Blue"
    
    # 2. RED RANGE (Hue is at both ends of the scale)
    if (h < 15 or h > 160) and s > 50:
        return "Red"

    # 3. WHITE (The "default" if no strong color is found)
    # If it's bright (High V) and has very little color (Low S)
    if s < 40 and v > 150:
        return "White"

    # 4. ML MODEL FALLBACK
    try:
        prediction = clf.predict([[h, s, v]])[0]
        return label_map.get(prediction, "Unknown")
    except:
        return "White" # Default to white if the AI is confused

@app.route('/predict', methods=['POST'])
def predict():
    try:
        img_bytes = request.get_data()
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None: return "Decode Error", 400

        cv2.imwrite("debug_snap.jpg", img)

        # Focus on a very small center square (50x50 pixels)
        # This prevents the white background/table from ruining the average color.
        h_img, w_img = img.shape[:2]
        center_roi = img[h_img//2 - 25 : h_img//2 + 25, w_img//2 - 25 : w_img//2 + 25]
        
        mean_val = cv2.mean(center_roi)[:3]
        hsv = cv2.cvtColor(np.uint8([[mean_val]]), cv2.COLOR_BGR2HSV)[0][0]
        
        result = get_color_prediction(hsv)
        print(f"Final Decision: {result}")
        return result

    except Exception as e:
        print(f"Error: {e}")
        return "White", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)