import cv2
image1 = cv2.imread("lol.png")
image2 = cv2.imread("coolimage.png")
image3 = cv2.imread("bang.png")
image4 = cv2.imread("nah.png")

'''
print("height of image1: ", image1.shape[0])
print("width of image1: ", image1.shape[1])


print("height of image2: ", image2.shape[0])
print("width of image2: ", image2.shape[1])

image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
blended = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)\
    

cv2.imshow("combined Images", blended)
'''

size = (200,200)

image1 = cv2.resize(image1, size)
image2 = cv2.resize(image2, size)
image3 = cv2.resize(image3, size)
image4 = cv2.resize(image4, size)

top_row = cv2.hconcat([image1, image2])
bottom_row = cv2.hconcat([image3, image4])
blended = cv2.vconcat([top_row, bottom_row])



cv2.imshow("combined Images", blended)
cv2.waitKey(0)
cv2.destroyAllWindows()