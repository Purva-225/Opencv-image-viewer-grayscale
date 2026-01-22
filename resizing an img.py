#Resizing An img

import cv2

IMAGE = cv2.imread("Image.png")

if IMAGE  is None:
    print("Image not found")
else:
    print("image not found")

    resized = cv2.resize(IMAGE,(300,300))

    cv2.imshow("Original image",IMAGE)
    cv2.imshow("resized image",resized)

    cv2.imwrite("resized_output.png",resized)

    cv2.waitKey(0)
    cv2.destroyAllWindoes()
