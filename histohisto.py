import cv2
import matplotlib.pyplot as plt

image_path = 'jas.jpg'
image =cv2.imread(image_path)

if image is None:
    print("Error: Could not load image")
    exit()

height, width = image.shape[:2]
scale = 600 / max(height, width)
display_image=  cv2.resize(image, None, fx=scale, fy=scale)


cv2.imshow('Image resized', image)

red_histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
green_histogram = cv2.calcHist([image], [1], None, [256], [0, 256])
blue_histogram = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(red_histogram, color='r')
plt.title('Red Histogram')

plt.subplot(3, 1, 2)
plt.plot(green_histogram, color='g')
plt.title('Green Histogram')

plt.subplot(3, 1, 3)
plt.plot(blue_histogram, color='b')
plt.title('Blue Histogram')

plt.tight_layout()
plt.show()


