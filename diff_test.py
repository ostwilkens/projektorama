# pylint: disable=invalid-name,missing-module-docstring
#%%
from time import sleep
import imutils.video
import cv2
import numpy as np

stream = imutils.video.WebcamVideoStream()
stream.start()
shape = stream.frame.shape
black = np.zeros(shape, dtype="uint8")

frame = stream.read()
new_frame = frame

while True:
    prev_frame = new_frame
    new_frame = stream.stream.read(True)[1]

    diff = cv2.absdiff(prev_frame, new_frame)

    # mask = cv2.GaussianBlur(diff, (5,5), 0)
    # frame = (np.clip(diff, 20, 255) - 20) * 2
    frame = diff
    # frame = cv2.fastNlMeansDenoisingColored(diff,None,10,10,7,21)


    cv2.imshow("window", frame)
    if cv2.waitKey(1) > 0:
        cv2.destroyAllWindows()
        stream.stream.release()
        break
