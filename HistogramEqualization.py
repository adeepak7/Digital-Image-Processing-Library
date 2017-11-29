import cv2
import numpy as np
import math


def convertToGrayscale(image_url):

    image_array = cv2.imread(image_url, cv2.IMREAD_UNCHANGED)
    temp_image_array = image_array
    no_of_rows = len(temp_image_array)
    # No. of columns:
    no_of_columns = len(temp_image_array[0])

    for i in range(0,no_of_rows):
        for j in range(0,no_of_columns):
            temp_image_array[i][j] = (0.114*image_array[i][j][0] + 0.587*image_array[i][j][1] +
                                      0.299*image_array[i][j][2])

    cv2.imshow('',temp_image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gray_scale_read(image_url):

    image_array = cv2.imread(image_url, cv2.IMREAD_UNCHANGED)

    cv2.imshow('', image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contrast_stretch(image_array)


def round_num(d=0.0):
    math.floor(float(d))


def contrast_stretch(image):
     # No. of rows
    no_of_rows = len(image)

    # No. of columns:
    no_of_columns = len(image[0])
    a = np.array([0.0 for i in range(256)])

    # Find frequency of each gray level
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            a[image[i][j]] += 1.0

    number_of_pixels = no_of_columns * no_of_rows
    # Find contribution of each gray level
    a /= float(number_of_pixels)

    # Find cumulative sum
    for i in range(1,256):
        a[i] += a[i-1]

    # For new mapping multiply it by 255
    a *= 255
    for i in range(256):
        a[i] = math.floor(a[i])

    for i in range(no_of_rows):
        for j in range(no_of_columns):
            image[i][j] = int(a[image[i][j]])

    cv2.imshow('Histogram Equalized Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
def main():
    print("Enter image url: ")
    gray_scale_read('A2_image3.tif')

main()
'''