import cv2
import numpy as np
import csv

# Open a CSV file to store our training data
csv_file = open('pill_data.csv', mode='a', newline='')
writer = csv.writer(csv_file)
# Uncomment the line below only the VERY FIRST time you run this to add headers:
# writer.writerow(['h', 's', 'v', 'label']) 

CAM_URL = "http://172.23.7.242:8080//video"
cap = cv2.VideoCapture(CAM_URL)

print("Press 's' to save data for: 0=Red, 1=Blue, 2=White. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: continue
    
    frame = cv2.resize(frame, (480, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(cv2.GaussianBlur(gray, (7, 7), 0), 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        if 10 < radius < 100:
            mask = np.zeros(frame.shape[:2], dtype="uint8")
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            
            # Get the HSV values
            mean_val = cv2.mean(frame, mask=mask)[:3]
            h, s, v = cv2.cvtColor(np.uint8([[mean_val]]), cv2.COLOR_BGR2HSV)[0][0]
            
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            cv2.putText(frame, f"H:{h} S:{s} V:{v}", (10, 30), 1, 1, (255,255,255), 1)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                label = input("Enter Label (0:Red, 1:Blue, 2:White): ")
                writer.writerow([h, s, v, label])
                print(f"Saved: {h}, {s}, {v} as {label}")
            break

    cv2.imshow("Data Collector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
csv_file.close()