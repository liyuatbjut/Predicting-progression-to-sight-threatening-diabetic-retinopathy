# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:40:37 2019

To Preprocess XML

@author: admin
"""



from xml.dom.minidom import Document
from xml.dom.minidom import parse
import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def CLAHE(imgFolder, outputFolder):
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    imgList = os.listdir(imgFolder)
    for imgFile in imgList:
        pre, ext = os.path.splitext(imgFile)
        if ext!=".JPG" and ext!=".jpg":
            print("{} is not JPG File".format(imgFile))
            continue
        inputFilePath = os.path.join(imgFolder, imgFile)
        outputFilePath = os.path.join(outputFolder, imgFile)

        img = cv.imread(inputFilePath)
        img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
        # 图像归一化
        img_input = img_yuv[:, :, 0]
        clahe = cv.createCLAHE(clipLimit=3, tileGridSize=(8, 8))
        img_output = clahe.apply(img_input)

        img_yuv[:, :, 0] = img_output
        imgG = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

        cv.imwrite(outputFilePath, imgG)


if __name__ == "__main__":
    imgFolder = r"C:\Users\hp\Desktop\graduate student final design\testimg\ori"
    outputFolder = r"C:\Users\hp\Desktop\graduate student final design\testimg\ycl"
    CLAHE(imgFolder, outputFolder)

