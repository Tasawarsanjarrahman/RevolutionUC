import cv2
import numpy as np
import joblib

# 1. Load the trained brain
try:
    clf = joblib.load('pill_model.pkl')
except:
    print("Model file not found! Run train_model.py first.")
    exit()

# Map the numbers back to names
label_map = {0: "Red", 1: "Blue", 2: "White"}

CAM_URL = "http://172.23.7.242:8080//video"
cap = cv2.VideoCapture(CAM_URL)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.resize(frame, (480, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        if 10 < radius < 100:
            # Create mask and get average color
            mask = np.zeros(frame.shape[:2], dtype="uint8")
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            mean_val = cv2.mean(frame, mask=mask)[:3]
            
            # Convert to HSV
            pill_hsv = cv2.cvtColor(np.uint8([[mean_val]]), cv2.COLOR_BGR2HSV)[0][0]
            h, s, v = pill_hsv

            # 2. ASK THE AI FOR THE ANSWER
            # We wrap [h, s, v] in double brackets because the model expects a list of samples
            prediction = clf.predict([[h, s, v]])[0]
            color_name = label_map.get(prediction, "Unknown")

            # Draw the results
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            cv2.putText(frame, f"AI: {color_name}", (int(x - radius), int(y - radius - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            break 

    cv2.imshow("ML Pill Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()