import  cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = cv2.imread('download.jpg', cv2.IMREAD_COLOR)
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

recognized_text = pytesseract.image_to_string(grey_image)
recognized_text = recognized_text.replace(" ", "").replace("\n", "")
print("recognized_text")
print(recognized_text)

_ , binary_image = cv2.threshold(grey_image, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(binary_image)
countors,  _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_with_contours = cv2.drawContours(image, countors, -1, (0, 140,0 ), 1)

cv2.imshow("Image with Contours", image_with_contours)
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()