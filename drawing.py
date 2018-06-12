'''
drawing a line, rectangle and a circle using openCV
'''

import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

#Drawing a Line(imgname, ptA, ptB, color in (R, G, B), width)
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Drawing a Rectangle(imgname, topleft coordinates, bottom right Coordinates, color in (R,G,B), width)
img = cv2.rectangle(img, (12, 12), (120, 85), (0, 0, 255), 8)
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Drawing a circle(imgname, centre coordinates, radisusSize, color in (R,G,B), width)
img = cv2.circle(img,(111, 222), 100, (0,255,0), 11)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
