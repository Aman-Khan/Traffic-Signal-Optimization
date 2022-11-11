import cv2
import time
import numpy as np
from datetime import date
from datetime import datetime

### Setup ####
def click_event(event, x, y, flag, prama):
    if(len(points)<4):
        if event == cv2.EVENT_LBUTTONDOWN:
            font = cv2.FONT_HERSHEY_SIMPLEX
            strxy = '* '+str(x)+' '+str(y)
            cv2.putText(img, strxy, (x,y), font, 0.5, (0,0,255), 1, cv2.LINE_AA)        
            cv2.imshow('Track Road',img)
            points.append((x,y))
    else:
        cv2.line(img, points[0], points[1], (0,255,0), 2, cv2.LINE_AA)
        cv2.line(img, points[1], points[2], (0,255,0), 2, cv2.LINE_AA)
        cv2.line(img, points[2], points[3], (0,255,0), 2, cv2.LINE_AA)
        print("**Coordinates Saved**")
        cv2.imshow('Track Road',img)


print('╔'+''.center(28,'═')+'╗')
print('║ Set Coordinates by marking ║')
print('╚'+''.center(28,'═')+'╝')

points = []

cap = cv2.VideoCapture('video.mp4')
while(cap.isOpened()):
    ret, frame=cap.read()
    cv2.imshow('Live Capture', frame)
    
    if(cv2.waitKey(1)==ord('s')):
        cv2.imwrite('road_Data.jpg', frame)
        break
cap.release()
cv2.destroyAllWindows()

img = cv2.imread('road_Data.jpg')
cv2.imshow('Track Road',img)
cv2.setMouseCallback('Track Road', click_event)
if(cv2.waitKey(0)==ord('q')):
    cv2.destroyAllWindows()

endCoordinates = []
endCoordinates.extend(points)
counterLine = []
counterLine.extend(endCoordinates[1:3])
