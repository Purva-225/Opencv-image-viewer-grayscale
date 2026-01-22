#flipped img
import cv2

image = cv2.imread("image0.3.jpeg")

if image is None:
   print("img is not loaded")
else:
    flipped_horizontal = cv2.flip(image,0)
    flipped_Vertical = cv2.flip(image,1)
    flipped_Both = cv2.flip(image,-1)

cv2.imshow("Orignal",image)
cv2.imshow("flipped_horizontal", flipped_horizontal)
cv2.imshow("flipped_Vertical", flipped_Vertical)
cv2.imshow("flipped_Both", flipped_Both)

cv2.waitKey(0)
cv2.destroyAllWindows
