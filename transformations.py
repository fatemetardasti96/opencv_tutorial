import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image-path")
args = vars(parser.parse_args())

img = cv.imread(args["image_path"])

def translateXY(img, x, y):
    translationMat = np.float32([[1, 0, x], [0, 1, y]])
    width, height = img.shape[1], img.shape[0]
    dimensions = (width, height)

    return cv.warpAffine(img, translationMat, dimensions)

# -x --> right
# -y --> up
# x --> left
# y --> down
translated = translateXY(img, -100, -100)
cv.imshow("translated", translated)

def rotate(img, angle, rotationPoint=None):
    height, width = img.shape[:2]
    dimensions = (width, height)

    if rotationPoint is None:
        rotationPoint = (width//2, height//2)

    rotationMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)

    return cv.warpAffine(img, rotationMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("rotated", rotated)

# flip
# flip code:
#   0: vertically
#   1: horizontally
#   -1: both
flipped = cv.flip(img, 0)
cv.imshow("flipped", flipped)




cv.waitKey(0)