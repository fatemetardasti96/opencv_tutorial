from multiprocessing.connection import wait
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path")
parser.add_argument("-v", "--video", type=int, default=False, required=True)
args = vars(parser.parse_args())

if args["video"]:
    #read video
    cap = cv.VideoCapture(args["path"])
    while True:
        is_ok, frame = cap.read()
        if is_ok:
            cv.imshow("video frame", frame)
            if cv.waitKey(20) & 0xFF == ord("q"):
                break
        else:
            break

else:
    #read image
    img = cv.imread(args["path"])
    cv.imshow("frame", img)

    cv.waitKey(0)
