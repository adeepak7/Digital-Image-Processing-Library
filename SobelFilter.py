import cv2
import ValidPosition
from copy import deepcopy

def sobelFilter(path):

    image = cv2.imread(path)

    print("Applying Sobel filter  to grayscale image...")

    temp_image1 = deepcopy(image)
    temp_image2 = deepcopy(image)

    # No. of rows:
    noOfRows = image.shape[0]

    # No. of columns:
    noOfColumns = image.shape[1]

    mask = [[-1,-2,-1], [0,0,0], [1,2,1]]

    for x in range(0, noOfRows):
        for y in range(0, noOfColumns):
            grayLevel = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    tmpx = x + i
                    tmpy = y + j
                    if ValidPosition.isValidPosition(tmpx, tmpy, noOfRows, noOfColumns):
                        grayLevel += mask[i - 1][j - 1]  * image[tmpx][tmpy][0]
            temp_image1[x][y] = abs(int(grayLevel))

    cv2.imshow('Sobel Filter along X-axis', temp_image1)
    cv2.waitKey(30)

    mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

    for x in range(0, noOfRows):
        for y in range(0, noOfColumns):
            grayLevel = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    tmpx = x + i
                    tmpy = y + j
                    if ValidPosition.isValidPosition(tmpx, tmpy, noOfRows, noOfColumns):
                        grayLevel += mask[i - 1][j - 1] * image[tmpx][tmpy][0]
            temp_image2[x][y] = abs(int(grayLevel))

    cv2.imshow('Sobel Filter along Y-axis', temp_image2)
    cv2.waitKey(30)

    for x in range(0, noOfRows):
        for y in range(0,noOfColumns):
            image[x][y] = temp_image1[x][y] + temp_image2[x][y]

    cv2.imshow('Sobel Filter along both axis', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
