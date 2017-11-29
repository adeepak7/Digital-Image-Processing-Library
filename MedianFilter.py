import cv2
import ValidPosition
from copy import deepcopy

def convertToGrayscale(image_url,size):
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

    applyMedianFilter(tempImageArray ,size)


def applyMedianFilter(imageArray, size,timeout=0):
    tempImageArray = deepcopy(imageArray)

    # No. of rows:
    noOfRows = len(tempImageArray)

    # No. of columns:
    noOfColumns = len(tempImageArray[0])
    size = (size - 1) //2
    for x in range(0, noOfRows):
        for y in range(0, noOfColumns):
            medianList = []
            for i in range(-size, size + 1, 1):
                for j in range(-size, size + 1, 1):
                    tmpx = x + i
                    tmpy = y + j
                    if ValidPosition.isValidPosition(tmpx, tmpy, noOfRows, noOfColumns):
                        medianList.append(imageArray[tmpx][tmpy][0])
            medianList.sort()
            tempImageArray[x][y][0] = medianList[len(medianList) // 2];
            tempImageArray[x][y][1] = medianList[len(medianList) // 2];
            tempImageArray[x][y][2] = medianList[len(medianList) // 2];

    cv2.imshow('Median Filtered Image', tempImageArray)
    cv2.waitKey(timeout)
    cv2.destroyAllWindows()

    return tempImageArray