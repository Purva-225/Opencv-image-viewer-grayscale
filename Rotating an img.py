#rotating an img
import cv2
    
image = cv2.imread("image0.1.png")

if image is None:
    print("could not load")
else:
     (h, w) = image.shape[:2]  
     center = (w / 2, h / 2)
     M = cv2.getRotationMatrix2D(center, 90, 0.1)

     Rotated = cv2.warpAffine(image, M, (w, h))  
     cv2.imshow("Original", image)
     cv2.imshow("Rotated", Rotated) 

     cv2.waitKey(0)
     cv2.destroyAllWindows()
