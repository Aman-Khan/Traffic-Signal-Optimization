import cv2
import numpy as np
from datetime import date
from datetime import datetime
from matplotlib import pyplot as plt

####################################
#    Take input to track road      #
####################################
cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
    ret, frame=cap.read()
    cv2.imshow('Live Capture', frame)
    
    if(cv2.waitKey(1)==ord('s')):
        cv2.imwrite('road_Data.jpg', frame) #capture frame
        break
cap.release()
cv2.destroyAllWindows()

points = [] #store coordinates of road for counter line
def click_event(event, x, y, flag, prama):
    if(len(points)<2):
        if event == cv2.EVENT_LBUTTONDOWN:
            font = cv2.FONT_HERSHEY_SIMPLEX
            strxy = '* '+str(x)+' '+str(y)
            cv2.putText(img, strxy, (x,y), font, 0.5, (0,0,255), 1, cv2.LINE_AA)        
            cv2.imshow('Track Road',img)
            points.append((x,y))
    else:
        print("**Coordinates Saved**")
        cv2.line(img, points[0], points[1], (0,255,0), 2, cv2.LINE_AA)
        cv2.imshow('Track Road',img)
        
        

img = cv2.imread('road_Data.jpg') #show track coordinates
cv2.imshow('Track Road',img)
cv2.setMouseCallback('Track Road', click_event)
if(cv2.waitKey(0)==ord('q')):
    cv2.destroyAllWindows()

print(points)

cap=cv2.VideoCapture('video.mp4') 
algo=cv2.createBackgroundSubtractorMOG2()

count_line_position=550
min_width_react=80
min_height_react=80

def center_handle(x,y,w,h):
  x1=int(w/2)
  y1=int(h/2)
  cx=x+x1
  cy=y+y1
  return cx,cy

detect=[]
offset=6
counter=0

while True:
    ret,frame1 = cap.read()
    grey=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(3,3),3)
    img_sub=algo.apply(blur)
    dilat=cv2.dilate(img_sub,np.ones((5,5)))
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatada=cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
    dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
    counterShape,_=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # cv2.line(frame1,(70,count_line_position),(980,count_line_position),(255,255,255),3)
    cv2.line(frame1,points[0],points[1],(255,255,255),3)

    cv2.line(frame1, (-150,730), (70,550), (25,0,255), 3, cv2.LINE_AA)
    cv2.line(frame1, (1175,730), (980,550), (25,0,255), 3, cv2.LINE_AA)


    for (i,c) in enumerate(counterShape):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter = (w>=min_width_react) and (h>=min_height_react)
        if not validate_counter:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

        center=center_handle(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1,center,4,(0,0,255),-1)

        for (x,y) in detect:
            if y<(count_line_position+offset) and y>(count_line_position-offset):
                counter+=1
                # cv2.line(frame1,(70,count_line_position),(980,count_line_position),(0,127,255),3)
                cv2.line(frame1,points[0],points[1],(0,127,255),3)

                detect.remove((x,y))
                print("VEHICLE COUNTER "+str(counter))
        #counter has value of num of vehicle
    today = date.today()
    now = datetime.now()
    cv2.putText(frame1,"VEHICLE COUNTER : "+str(counter),(900,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2, cv2.LINE_AA)
    cv2.putText(frame1, now.strftime("%H:%M:%S"), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)
    cv2.putText(frame1, today.strftime("%d-%m-%y"), (90,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)
    
    cv2.imshow('Video original',frame1)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
