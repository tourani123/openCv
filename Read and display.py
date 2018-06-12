'''
Contains code to do the following operations in python using openCV
-> Reading an image
-> Displaying an image
'''

import numpy as np
import cv2

# Reading image in grayScale
img = cv2.imread("depth.jpg", 0)

#Display image
cv2.imshow('Our Image ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
