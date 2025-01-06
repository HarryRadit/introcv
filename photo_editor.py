import cv2

image_path = 'me.jpg'

image = cv2.imread(image_path)

def crop_image(image,x,y,w,h):
    cropped_image = image[y:y+h, x:x+w]
    return cropped_image

cropped_image = crop_image(image, 300, 150, 700, 900)
def resize_image(image, scale_percentage):
    width = int(image.shape[1] * scale_percentage / 100)
    height = int(image.shape[0] * scale_percentage / 100)
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def rotate_image(image, angle):
    center = (image.shape[1] / 2, image.shape[0] / 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

    return rotated_image

resized_image = resize_image(cropped_image, 70)
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', resized_image)
cv2.imshow('Rotated Image', rotate_image(resized_image, 90))
cv2.waitKey(0)
cv2.destroyAllWindows()

