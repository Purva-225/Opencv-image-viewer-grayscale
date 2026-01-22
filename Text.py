import cv2

image = cv2.imread("image.png")

if image is None:
    print("OOPS! image is not working")
else:
    print("Img loaded succefully")
    cv2.putText(image,"This is  a Text",(40,300),
         cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0), 2)
    cv2.imshow("text",image)
    cv2.waitKey(0)
    cv2.distroyAllWindows()
