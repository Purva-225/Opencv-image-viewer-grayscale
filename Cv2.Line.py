#cv2.Line
import cv2

image = cv2.imread("image.png")

if image is None:
    print("Oops!Image is not working")
else:
    print("Image Loaded Successfully")

    pt1 = (100,200)
    pt2 = (225, 22)
    color = (255,0,0)
    thickness = 4

    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindow
