import os
import cv2
from PIL import Image 
from getHSVcolor import get_limits

# leer video
video = cv2.VideoCapture(os.path.join('.', 'assets', 'green-objects.mp4'))

BGR_COLOR = [0, 255, 0]
lowerLimit, upperLimit = get_limits(BGR_COLOR)

# ver video
ret = True
while ret:
  ret, frame = video.read()
  if ret:
    resized_frame = cv2.resize(frame, (960, 540))

    hsvFrame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvFrame, lowerLimit, upperLimit)

    maskPIL = Image.fromarray(mask)

    bbox = maskPIL.getbbox()

    if bbox is not None:
      x1, y1, x2, y2 = bbox

      cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
    
    cv2.imshow('video', resized_frame)
    cv2.waitKey(33)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video.release()
cv2.destroyAllWindows()
