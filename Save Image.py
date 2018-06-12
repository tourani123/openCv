'''
Contains code to do the following operations in python using openCV
-> Save Image
'''

import numpy as np
import cv2

# Reading image in grayScale
img = cv2.imread("depth.jpg", 0)
#Display image
cv2.imwrite("Depth in grayScale.png", img)
cv2.destroyAllWindows()
