import cv2
import numpy as np

points =[]
mask = None
dots = None
shapes = []

image_path = 'DusttaleImpostor_Phase_22.webp'
image = cv2.imread(image_path)
mask = np.zeros_like(image)
dots = np.zeros_like(image)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

def draw_freehand(event, x, y, flags, param):
    global  points

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(dots, (x, y), 2, (255, 255, 255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:...

    elif event == cv2.EVENT_LBUTTONUP:...

cv2.namedWindow('Freehand selection')
cv2.setMouseCallback('Freehand selection', draw_freehand)


while True:
    combined_image = cv2.addWeighted(image, 0.7, mask, 0.3, 0)
    combined_image = cv2.addWeighted(combined_image, 0.7, mask, 0.3, 0)
    cv2.imshow('Image combined', combined_image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('x'):
        points = []
        shapes = []
        mask = np.zeros_like(image)
        dots = np.zeros_like(image)

    elif key == ord('e'):
        if len(points) == 2:
            radius = int(cv2.norm(np.array(points[-1]) - np.array(points[1]) - np.array(points[0])))
            cv2.circle(mask, points[0], radius, (255, 255, 255), -1)
            circle_points = cv2.ellipse2Poly(points[0], (radius,radius), 0, 0, 360,1)
            shapes.append(circle_points)
            dots = np.zeros_like(image)
            points = []

            cv2.fillPoly(dots, shapes, (255,255,255))
            selected_area = cv2.bitwise_and(image,mask)
            cv2.imshow('Selected area', selected_area)




    elif key == ord('q'):
        break