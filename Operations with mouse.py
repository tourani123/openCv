'''
    Performing operations with mouse
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Contains all mouse events/operations
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def drawCircleButtonClick(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img, (x, y), 30, (244, 244, 111,), 2)


img = np.zeros((512, 100, 3), np.uint8)

cv2.namedWindow("black background mouse operations")
cv2.setMouseCallback('black background mouse operations', drawCircleButtonClick)

while(1):
    cv2.imshow('black background mouse operations', img)
    if(cv2.waitKey(20) & 0xFF == 27): # Press Escape key to exit
        break

cv2.destroyAllWindows()
