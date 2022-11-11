import cv2 
import time
from datetime import datetime 
from datetime import date

cap=cv2.VideoCapture('video.mp4')

flag = True

dur = 5
start = time.time()
g_time = 5

while flag:
    ret,frame1 = cap.read()
    swtime = "{:02d}".format(dur-int(time.time()-start))

    today = date.today()
    now = datetime.now()
    cv2.putText(frame1, now.strftime("%H:%M:%S"), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)
    cv2.putText(frame1, today.strftime("%d-%m-%y"), (90,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)

    cv2.rectangle(frame1,(70,72),(90,210),(0,0,0),50, cv2.LINE_AA)

    if(time.time()<=start+dur-3):
        cv2.circle(frame1,(80,80),10,(0,0,255),30, cv2.LINE_AA)
        cv2.putText(frame1, swtime, (60,89), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
    elif(time.time()>start+dur-3 and time.time()<=start+dur):
        cv2.circle(frame1,(80,140),10,(0,255,255),30, cv2.LINE_AA)
        cv2.putText(frame1, swtime, (60,149), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
    else:
        cv2.circle(frame1,(80,200),10,(0,255,0),30, cv2.LINE_AA)
        cv2.putText(frame1, "{:02d}".format(int(swtime)+g_time), (60,209), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
        if(int(swtime)+g_time<=0):
            start=time.time()
    cv2.imshow('Video original',frame1)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
