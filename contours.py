import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image-path")
args = vars(parser.parse_args())

img = cv.imread(args["image_path"])
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 100, 200, 0)
cv.imshow("thresh", thresh)

blur = cv.GaussianBlur(img, (3,3), sigmaX=5, sigmaY=5)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contr_img = cv.drawContours(img, contours, -1, (0,0,255), 1)
cv.imshow("contours canny", contr_img)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contr_img = cv.drawContours(img, contours, -1, (0,0,255), 1)
cv.imshow("contours thresh", contr_img)

cv.waitKey(0)