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
currentFrameWeight = 0.05

while True:
    sleep(1.0 / 20.0)
    newFrame = cv2.multiply(stream.read(), np.array([1.3]))
    frame = cv2.addWeighted(
        newFrame, currentFrameWeight, frame, 1.0 - currentFrameWeight, 1.0
    )
    cv2.imshow("window", frame)
    if cv2.waitKey(1) > 0:
        cv2.destroyAllWindows()
        stream.stream.release()
        break
