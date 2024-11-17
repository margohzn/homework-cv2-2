import cv2 

churose = cv2.imread("churose.jpg")

churose1 = cv2.GaussianBlur(churose, (5,5), 0) # fades image
churose2 = cv2.medianBlur(churose, 7) # softens edges 
churose3 = cv2.bilateralFilter(churose, 5, 20, 20) # makes image sharper
churose4 = cv2.copyMakeBorder(churose, 20,20,20,20, cv2.BORDER_CONSTANT, value = (205,203,255)) # makes border of image

#rectangle 
left_top = (40,40)
right_bottom = (300,100)
color = (255,255,255)
thickness = 10
churose = cv2.rectangle(churose, left_top, right_bottom, color, thickness)

#text 
origin = (60,80)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 2
color = (0,0,0)
thickness = 3
churose = cv2.putText(churose, "Churose:", origin, font, fontScale, color, thickness, cv2.LINE_AA)\

#circle
center_coordinate = (60, 150)
radius = 20
color = (255,255,255)
thickness = 2
churose = cv2.circle(churose, center_coordinate, radius, color, thickness)

cv2.imshow("Churose", churose)
cv2.imshow("Chruose gaussian blur", churose1)
cv2.imshow("Churose median blur", churose2)
cv2.imshow("Churose bilateral blur", churose3)
cv2.imshow("Churose border", churose4)

cv2.waitKey(0)
cv2.destroyAllWindows