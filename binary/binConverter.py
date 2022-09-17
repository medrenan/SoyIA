import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/0b2bdc2d-4df2-4b86-a396-cb0325ea269b_1.jpg',2)


ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

plt.imshow(img)
cv2.imshow("Binary Image",bw_img)


cv2.waitKey(0)
cv2.destroyAllWindows()