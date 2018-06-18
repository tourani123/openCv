#https://www.learnopencv.com/alpha-blending-using-opencv-cpp-python/

import cv2

# Read the foreground image with alpha channel
foreGroundImage = cv2.imread("foreGroundAsset.png" ,-1)

#print(foreGroundImage.shape)

# Split png foreground image
b,g,r,a = cv2.split(foreGroundImage)


# Save the foregroung RGB content into a single object
foreground = cv2.merge((b,g,r))

# Save the alpha information into a single Mat
alpha = cv2.merge((a,a,a))


cnt = 0
nCnt = 0
fullShape = alpha.shape[0] * alpha.shape[1] * alpha.shape[2]
print("What is :" , fullShape)

'''
for i in range(alpha.shape[0]):
        for j in range(alpha.shape[1]):
                for k in range(alpha.shape[2]):
                        if(alpha[i][j][k] > 0.0):
                                cnt = cnt + 1
                        else:
                                nCnt = nCnt + 1

print("Cnt is =>", cnt, nCnt, fullShape - cnt) 
'''

#print("Alpha Size => ", alpha.shape, "Foreground Shape =>", foreground.shape)

# Read background image
background = cv2.imread("backGround.jpg")

#print("Background shape =>", background.shape)

# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
alpha = alpha.astype(float)/255
#foreground = foreground.astype(float)/255

# Perform alpha blending
foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)
outImage = cv2.add(foreground, background)

outImage = outImage.astype(float)/255
cv2.imwrite("outImgPy.png", outImage)

cv2.imshow("outImg", outImage)
cv2.waitKey(0)

cv2.destroyAllWindows()
