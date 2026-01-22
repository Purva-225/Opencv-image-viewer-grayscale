import cv2

image = cv2.imread("image.png")

if image is None:
    print("OOPS! image doest work")
else:
    print("Image loaded successfully")

    cv2.circle(image,(250,150), 50, (210,150), 5)
    cv2.imshow("Circle Drawing", image)
    cv2.waitKey(0)
    cv2.distroyAllWindows()
