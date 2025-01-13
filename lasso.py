import cv2
import numpy as np

drawing  = False
points = []
mask = None

image_path = 'DusttaleImpostor_Phase_22.jpg'

image = cv2.imread(image_path)

def draw_freehand(event, x, y, flags, param):
    global drawing, points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points = [(x, y)]
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            points.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points.append((x, y))
        cv2.fillPoly(mask, [np.array(points)], (182,200,255))

mask = np.zeros_like(image)

cv2.namedWindow('Freehand selection')
cv2.setMouseCallback('Freehand selection', draw_freehand)

while True:
    cv2.imshow('Freehand selection', cv2.addWeighted(image, 0.7, mask, 0.3, 0))
    key = cv2.waitKey(1) & 0xFF

    if key == ord('x'):
        mask = np.zeros_like(image)
    elif key == ord('2'):
        break

selected_area = cv2.bitwise_and(image,mask)

cv2.imshow('Selected area', selected_area)
cv2.waitKey(0)
cv2.destroyAllWindows()