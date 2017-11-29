import cv2
import ValidPosition
from copy import deepcopy
import MedianFilter

def laplacianFilter(path):

    image = cv2.imread(path)

    print("Applying laplacian filter  to grayscale image...")

    image = MedianFilter.applyMedianFilter(image, 3 , 1)

    temp_image = deepcopy(image)

    # No. of rows:
    noOfRows = image.shape[0]

    # No. of columns:
    noOfColumns = image.shape[1]

    mask = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]

    for x in range(0, noOfRows):
        for y in range(0, noOfColumns):
            grayLevel = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    tmpx = x + i
                    tmpy = y + j
                    if ValidPosition.isValidPosition(tmpx, tmpy, noOfRows, noOfColumns):
                        grayLevel += mask[i - 1][j - 1]  * image[tmpx][tmpy][0]
            temp_image[x][y] = int(grayLevel)

    cv2.imshow('Lalacian Filtered Image', temp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
