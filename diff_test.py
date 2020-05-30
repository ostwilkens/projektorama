# pylint: disable=invalid-name,missing-module-docstring
#%%
from time import sleep
import imutils.video
import cv2
import numpy as np

stream = imutils.video.WebcamVideoStream()
stream.start()
# shape = stream.frame.shape
# black = np.zeros(shape, dtype="uint8")

frame = stream.read()

while True:
    sleep(1.0 / 30.0)

    prev_frame = new_frame
    new_frame = stream.read()

    diff = cv2.absdiff(prev_frame, new_frame)

    mask = cv2.GaussianBlur(diff, (5,5), 0)

    frame = np.clip(mask * 10, 0, 255)
    # frame = diff * 100
    # frame = 255 - diff

    cv2.imshow("window", frame)
    if cv2.waitKey(1) > 0:
        cv2.destroyAllWindows()
        stream.stream.release()
        break