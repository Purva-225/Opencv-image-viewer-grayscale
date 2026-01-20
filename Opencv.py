import cv2 
  
A1 = cv2.imread("image.png")

if A1 is None:
    print("Error: Image not found")
else:
    print("Image found successfully")

if A1 is not None:
  gray = cv2.cvtColor(A1, cv2.COLOR_BGR2GRAY)
   
  Choice = input("Enter 's' to save and 'v' to view: ").lower()
  #cv2.imshow("Original image", A1)
if Choice == 'v':
  cv2.imshow("Grayscale Image", gray)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

elif Choice == 's':
   cv2.imwrite("gray_image.png",gray)
   print("GrayScale image save as gray image.png")
else:
 print("invalid choice! please enter 'S' or 'V' ")
