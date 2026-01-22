import cv2

image = cv2.imread("image.png")

if image is None:
    print("OOPES! img not loaded succesfully")
else:
    print("img loaded successfully")

    pt1 = (1000,100)
    pt2 = (250, 200)
    color = (0,0,255)
    thickness = 3

    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("rectangle drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows
