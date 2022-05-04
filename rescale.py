from turtle import width
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path")
parser.add_argument("-v", "--video", type=int, default=False, required=True)
args = vars(parser.parse_args())


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

if args["video"]:
    #read video
    cap = cv.VideoCapture(args["path"])
    while True:
        is_ok, frame = cap.read()
        if is_ok:
            resized_frame = rescale_frame(frame, 0.5)
            cv.imshow("video frame", frame)
            cv.imshow("video frame resized", resized_frame)
            if cv.waitKey(20) & 0xFF == ord("q"):
                break
        else:
            break

else:
    #read image
    img = cv.imread(args["path"])
    resized_frame = rescale_frame(img)
    cv.imshow("frame", img)
    cv.imshow("resized frame", resized_frame)

    cv.waitKey(0)

