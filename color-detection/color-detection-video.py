import os
import cv2
# leer video
video = cv2.VideoCapture(os.path.join('.', 'assets', 'green-objects.mp4'))
# ver video
ret = True
while ret:
  ret, frame = video.read()
  resized_frame = cv2.resize(frame, (960, 540))

  if ret:
    cv2.imshow('video', resized_frame)
    cv2.waitKey(33)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video.release()
cv2.destroyAllWindows()
