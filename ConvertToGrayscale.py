import cv2
from copy import deepcopy

def convertToGrayscale(image_url):

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


    cv2.imshow('Grayscale Original Image',tempImageArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
