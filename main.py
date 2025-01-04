import cv2
import tkinter as tk
from tkinter import filedialog
def apply_grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image
image_path =  'nas.jpg'
image = cv2.imread(image_path)

def show_img():
    image_path = 'nas.jpg'
    image = cv2.imread(image_path)
    #Disply the image in a window
    cv2.imshow('Image', image)
    grayscale_image = apply_grayscale(image)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def show_img2():
    root = tk.Tk()
    root.withdraw()
    image_path = "nas.jpg"
    image_path2 = "nas2.jpg"
    image_path3 = "jas.jpg"
    image = cv2.imread(image_path)
    image2 = cv2.imread(image_path2)
    image3 = cv2.imread(image_path3)
    cv2.imshow('Image', image)
    cv2.imshow('ImageA', image2)
    cv2.imshow('ImageAA', image3)
    grayscale_image = apply_grayscale(image)
    grayscale_image2 = apply_grayscale(image2)
    grayscale_image3 =  apply_grayscale(image3)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('Grayscale Image', grayscale_image2)
    cv2.imshow('Grayscale Image', grayscale_image3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






if (__name__ == '__main__'):
    show_img2()

