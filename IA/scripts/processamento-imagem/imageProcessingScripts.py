from skimage.transform import resize
from matplotlib import pyplot as plt

import cv2

def transformImageToSquareWithPadding(self,image):
    height, width, channels = image.shape

    if height>width:
        sizeOffset = height-width
        paddingSizeForEachSide = int(sizeOffset/2)
        image = cv2.copyMakeBorder(image, 0, 0,paddingSizeForEachSide, paddingSizeForEachSide, cv2.BORDER_CONSTANT)

    if height<width:
        sizeOffset = width-height
        paddingSizeForEachSide = int(sizeOffset/2)
        image = cv2.copyMakeBorder(image, paddingSizeForEachSide, paddingSizeForEachSide,0, 0, cv2.BORDER_CONSTANT)

    return image


def resizeImageSameSize(self,image):
    image_downscaled = resize(image, (256, 256,3))
    return image_downscaled

def preProcessing(self,image_path):
    image = cv2.imread(image_path)

    image = transformImageToSquareWithPadding(image)
    image = resizeImageSameSize(image)
    image = binaryFilter(image)

    return image

def binaryFilter(self,image):
    bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return bw_img