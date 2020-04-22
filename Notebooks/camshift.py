import cv2
import numpy

img = cv2.imread("Camshiftsample.jpeg")

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("it is running here")
        cv2.circle(img,(x,y),100,(22,225,0),-1)



cv2.namedWindow(winname="finger")

cv2.setMouseCallback('finger',draw_circle)


while 1:
    cv2.imshow('finger',img)

    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
