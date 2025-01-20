import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = cv2.imread('Screenshot 2024-12-29 203538.png', cv2.IMREAD_COLOR)
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

recognized_text = pytesseract.image_to_string(grey_image)
print("recognized_text")
print(recognized_text)