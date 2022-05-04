import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image-path")
args = vars(parser.parse_args())

img = cv.imread(args["image_path"])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blurred = cv.GaussianBlur(img, (7,7), 10)
cv.imshow("blur", blurred)

canny = cv.Canny(blurred, 100, 100)
cv.imshow("edge", canny)

resized = cv.resize(img, (100, 100))
cv.imshow("resized", resized)

cropped = img[200:300, 100:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)