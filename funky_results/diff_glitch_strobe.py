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

    prev_frame = frame
    new_frame = stream.read()

    diff = cv2.absdiff(prev_frame, new_frame)

    frame = diff

    cv2.imshow("window", frame)
    if cv2.waitKey(1) > 0:
        cv2.destroyAllWindows()
        stream.stream.release()
        break