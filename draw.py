import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3))
# cv.imshow("blank", blank)

# draw rectangle
rect = cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), -1)
# cv.imshow("rectangle", rect)

# draw circle
circ = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 30, (0, 0, 255), 2)
# cv.imshow("circle", circ)

# draw line
line = cv.line(blank, (500, 500), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), 5)
# cv.imshow("line", line)

# write text
txt = cv.putText(blank, "Hello World!", (0, 250), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 250, 255), 1)
cv.imshow("text", txt)

cv.waitKey(0)