import tkinter
import numpy as np
import cv2
from tkinter import filedialog as fd

#Importing all the modules:
import testModule
import GaussianFilter
import ConvertToGrayscale
import MedianFilter
import HistogramEqualization
import LaplacianFilter
import SobelFilter

class ImagePrcessingBasics:

    #Data members of class:
    colouredImage = 0
    grayscaleImage = 0
    filename=""


    def __init__(self,colourValue,grayscaleValue):
        self.colouredImage = colourValue
        self.grayscaleImage = grayscaleValue


    def printSomething(self):

        print("*********** Welcome to Image Processing Library ***********")
        print("")


        while(True):

            object = ImagePrcessingBasics(0, 1)

            print("Select operations from the menu:")

            print("1: Set image type: ")

            print("2: Select the image you want to process on:")

            print("3: Select opeartions:")

            print("4: Exit application.")

            print("5: Your Option:")

            optionType = int(input())
            print(optionType)

            if(optionType == 1):
                print("Press 'C' for colour, 'G' for grayscale : ")
                imageType = input()
                if(imageType == 'C'):
                    object = ImagePrcessingBasics(1, 0)
                else:
                    object = ImagePrcessingBasics(0, 1)

                print("-----------------------------------------------")
                print("Image type Successfully configured.")
                print("-----------------------------------------------")

            elif(optionType == 2):
                filename = fd.askopenfilename()
                print("-----------------------------------------------")
                print("Path of image selected:%s"%filename)
                print("-----------------------------------------------")


            elif(optionType == 3):
                print("Select the type of operation:")
                print("1: Convert to grayscale.")
                print("2: Gaussian Filter.")
                print("3: Median Filter.")
                print("4: Histogram Equalization.")
                print("5: Laplacian Filter.")
                print("6: Sobel Filter.")
                print(" : Your Option : ")

                operationType = int(input())

                if 2<=operationType<=3:
                    print("Define size of mask:")
                    maskSize = int(input())


                if(operationType == 1):
                    ConvertToGrayscale.convertToGrayscale(filename)
                elif(operationType == 2):
                    GaussianFilter.convertToGrayscale(filename,maskSize)
                elif(operationType == 3):
                    MedianFilter.convertToGrayscale(filename,maskSize)
                elif(operationType == 4):
                    HistogramEqualization.gray_scale_read(filename)
                elif(operationType == 5):
                    LaplacianFilter.laplacianFilter(filename)
                elif (operationType == 6):
                    SobelFilter.sobelFilter(filename)

            elif(optionType == 4):
                print("-----------------------------------------------")
                print("Exited Library")
                print("-----------------------------------------------")
                break

def main():

    a = ImagePrcessingBasics(1,0)
    a.printSomething()


main()