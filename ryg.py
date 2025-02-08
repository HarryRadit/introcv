import cv2
import numpy  as np

red_lower = np.array([0, 100, 100], np.uint8)
red_upper = np.array([10, 255, 255], np.uint8)

blue_lower = np.array([110, 100, 100], np.uint8)
blue_upper = np.array([130, 255, 255], np.uint8)

black_lower = np.array([0, 0, 0], np.uint8)
black_upper = np.array([180, 255, 46], np.uint8)

image_path = "GROUP_WHITE_SPONSOR_JPG_00003.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Image not found: {image_path}")
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

red_mask = cv2.inRange(hsv, red_lower, red_upper)
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
black_mask = cv2.inRange(hsv, black_lower, black_upper)

kernel = np.ones((5, 5), np.uint8)
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)

opntours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
opntours_blue, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
opntours_black, _  = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in opntours_red:
    area = cv2.contourArea(contour)
    if area > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

for contour in opntours_blue:
    area = cv2.contourArea(contour)
    if area > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

for countour in opntours_black:
    area = cv2.contourArea(countour)
    if area > 500:
        x, y, w, h = cv2.boundingRect(countour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cv2.putText(img, "Black", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()