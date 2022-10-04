from skimage.transform import resize
from matplotlib import pyplot as plt
import numpy as np

import cv2

def transformImageToSquareWithPadding(image):
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


def resizeImageSameSize(image):
    image_downscaled = resize(image, (256, 256,3))
    return image_downscaled

def preProcessing(image_path):
    image = cv2.imread(image_path)
    print("image type CV2:",type(image))
    image = transformImageToSquareWithPadding(image)
    print("image type TRANSFORM:",type(image))
    image = resizeImageSameSize(image)
    print("image type RESIZE:",type(image))
    #image = binaryFilter(image)
    #print("image type BINARY:",type(image))



    return image

def binaryFilter(image):
    bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    bw_img =np.array(bw_img)
    return bw_img