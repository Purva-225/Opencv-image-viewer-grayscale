# user -> file location input -> u have to give many options like LINE, CIRCLE,RECTANGLE, TEXT

import cv2

image = input("Enter The File Location: ")
if image is None:
    print("Sorry! Image is not working ")
else:
    print("Image loaded successfuly")
    shape = input("What you have to Draw on it like: LINE, CIRCLEC RECTANGLE,TEXT: ")
    X1 = int(input("Enter X1 coordinate: "))
    Y1 = int(input("Enter Y1 coordinate: "))
    X2 = int(input("Enter X2 coordinate: "))
    Y2 = int(input("Enter Y2 coordinate: "))
    radius = int(input("Enter Radius: "))
    save_file = input("Do you want to save the file? (YES/NO): ")

    pt1 = (X1,Y1)
    pt2 = (X2, Y2)
    Font = input("Enter Font: ")
    Fontscale = float(input("Fontscale: "))
    color = (0,225,0)
    thickness = 4
    
    if shape.lower() == "line":
        cv2.line(image, pt1, pt2, color, thickness)
        cv2.imshow("Line Drawing", image)
    elif shape.lower() == "circle":
        cv2.circle(image, pt1, radius, color, thickness)  
        cv2.imshow("Circle Drawing", image)
    elif shape.lower() == "rectangle":
        cv2.rectangle(image, pt1, pt2, color, thickness)  
        cv2.imshow("Rectangle Drawing", image)
    elif shape.lower() == "text":
        cv2.putText(image, "Sample Text", pt1, cv2.FONT_HERSHEY_SIMPLEX, Fontscale, color, thickness)  
        cv2.imshow("Text Drawing", image)
        if save_file.lower() == "yes":
         cv2.imwrite("output_image.png", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
