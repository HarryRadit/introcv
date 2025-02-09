import cv2
import numpy as np
import os
import imutils
import pytesseract
import pandas as pd
import time
import re

import_folder = 'ting'
actual_data = pd.read_csv('ting/actual_data.csv', sep=';')
print(actual_data.columns)

data_to_append = []


def process_image(image_path):
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=600)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    countours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    countours = sorted(countours, key=cv2.contourArea, reverse=True)

    for c in countours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            NumberPlateCnt = approx
            break
    mask = np.zeros(gray_image.shape, np.uint8)
    mask = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)

    new_image = cv2.bitwise_and(image, image, mask=mask)
    config = ('-l eng --oem 1 --psm 3')
    detected_plate = pytesseract.image_to_string(new_image, config=config)

    detected_plate = detected_plate.replace(" ", "").replace("\n", "")
    detected_plate = re.sub(r'[^\w\s]', '', detected_plate)

    return detected_plate

for image_file in os .listdir(import_folder):
    if image_file.endswith('.jpg'):
        image_path = os.path.join(import_folder, image_file)
        print(image_path)

        actual_plate = actual_data[actual_data['image_file'] == image_file]['actual_number_plate'].values[0]

        print(actual_plate)

        detected_plate = process_image(image_path)
        print(detected_plate)

        if actual_plate == detected_plate:
            print("Correct")
        else:
            print("Incorrect")


        time.sleep(1)
        print()