import cv2
from matplotlib import pyplot as plt
import math
from copy import deepcopy

import ValidPosition

PI = 3.14159265359
exp = 2.718281828459045


def convertToGrayscale(image_url,size):

    print("Converting to grayscale...")

    imageArray = cv2.imread(image_url, cv2.IMREAD_UNCHANGED)

    print(type(imageArray))

    tempImageArray = deepcopy(imageArray)

    # No. of rows:
    noOfRows = len(tempImageArray)

    # No. of columns:
    noOfColumns = len(tempImageArray[0])

    for i in range(0, noOfRows):
        for j in range(0, noOfColumns):
            tempImageArray[i][j] = (
            0.114 * tempImageArray[i][j][0] + 0.587 * tempImageArray[i][j][1] + 0.299 * tempImageArray[i][j][2])


    cv2.imshow('Original Image', tempImageArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Converted to grayscale successfully")

    gaussianFilter(tempImageArray,size)


def gaussianFunction(x, y, delta):
    val = 1 / (2 * PI * (delta ** 2))
    val *= exp ** -((x ** 2 + y ** 2) / (2.0 * (delta ** 2)))

    return math.ceil(255.0 * float(val))


def gaussianFilter(imageArray, size):

    print("Applying gaussian filter  to grayscale image...")

    tempImageArray = deepcopy(imageArray)

    # No. of rows:
    noOfRows = len(tempImageArray)

    # No. of columns:
    noOfColumns = len(tempImageArray[0])
    mid = (size - 1) / 2
    mask = []
    maskSum = 0.0

    for i in range(0, size):
        x = []
        for j in range(0, size):
            gauss = gaussianFunction(mid - i, mid - j, 1)
            x.append(gauss)
            maskSum += gauss
        mask.append(x)

    size = (size - 1) / 2
    for x in range(0, noOfRows):
        for y in range(0, noOfColumns):
            grayLevel = 0
            for i in range(-size, size + 1, 1):
                for j in range(-size, size + 1, 1):
                    tmpx = x + i
                    tmpy = y + j
                    if ValidPosition.isValidPosition(tmpx, tmpy, noOfRows, noOfColumns):
                        grayLevel += mask[i + size][j + size] * (1.0) * imageArray[tmpx][tmpy][0]
            tempImageArray[x][y][0] = int((1.0 / maskSum) * grayLevel)
            tempImageArray[x][y][1] = int((1.0 / maskSum) * grayLevel)
            tempImageArray[x][y][2] = int((1.0 / maskSum) * grayLevel)

    cv2.imshow('Gaussian Filtered Image', tempImageArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
