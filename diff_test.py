# pylint: disable=invalid-name,missing-module-docstring

# #%%
# import cv2
# cap = cv2.VideoCapture(0)
# # cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# # cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
# # cap.set(cv2.CAP_PROP_SETTINGS, 1)
# cap.set(cv2.CAP_PROP_AUTOFOCUS,0)
# cap.set(cv2.CAP_PROP_FOCUS,10)
# cap.set(cv2.CAP_PROP_EXPOSURE,5)

#%%
from time import sleep
import imutils.video
import cv2
import numpy as np
from datetime import datetime
from math import sin, cos, tan

stream = imutils.video.WebcamVideoStream()
stream.start()
shape = stream.frame.shape
black = np.zeros(shape, dtype="uint8")

frame = stream.read()
new_frame = frame

cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

start_time = datetime.now()

while True:
    elapsed = (datetime.now() - start_time).total_seconds()
    n = elapsed * 2
    prev_frame = new_frame
    new_frame = stream.stream.read(True)[1]

    diff = cv2.absdiff(prev_frame, new_frame)

    # mask = cv2.GaussianBlur(diff, (5,5), 0)
    # frame = (np.clip(diff, 20, 255) - 20) * 2
    # frame = (diff * 0.5)
    # frame = cv2.fastNlMeansDenoisingColored(diff,None,10,10,7,21)

    # frame = diff
    frame = new_frame
    # frame = cv2.multiply(frame, np.array([0.5])) #mul

    frame = 255 - frame #invert

    # margin = -20 + int(sin(n) * 20) 
    margin = -10


    x = 170 + margin # + int(sin(n * 0.8) * 10) 
    y = 125 + margin # + int(cos(n * 0.5) * 10)
    w = 318 - margin * 2
    h = 220 - margin * 2
    frame = frame[y:y+h, x:x+w]

    cv2.imshow("window", frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        stream.stream.release()
        break
