#CROP AN IMG 
import cv2

image = cv2.imread("image0.1.png")

if image is not None: 
 cropped = image[20: 1000,50:50]
 cv2.imshow("original",image)
 cv2.imshow("cropped", image)
 cv2.waitKey(0)
 cv2.destroyAllWindows
