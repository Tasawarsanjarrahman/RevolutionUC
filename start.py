import cv2
import numpy as np

CAM_URL = "http://172.23.7.242:8080//video"

cap = cv2.VideoCapture(CAM_URL)
if not cap.isOpened():
    print("Failed to open camera stream!")
    exit()

# Map HSV hue ranges to only white, red, and blue
def get_color_name_hsv(h, s, v):
    if v < 50:
        return "dark"
    if s < 50:
        return "white"
    if h < 10 or h > 160:
        return "red"
    elif 85 <= h < 140:
        return "blue"

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.resize(frame, (480, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_pill = False

    for cnt in contours:
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        if radius < 10 or radius > 100:
            continue

        mask = np.zeros(frame.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [cnt], -1, 255, -1)

        mean_val = cv2.mean(frame, mask=mask)[:3]
        pill_hsv = cv2.cvtColor(np.uint8([[mean_val]]), cv2.COLOR_BGR2HSV)[0][0]
        h, s, v = pill_hsv
        color_name = get_color_name_hsv(h, s, v)

        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
        cv2.putText(frame, color_name, (int(x - radius), int(y - radius - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        detected_pill = True
        break  # Only first pill

    if not detected_pill:
        cv2.putText(frame, "No pill detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Pill Detection HSV", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()