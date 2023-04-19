import cv2

### Setup ####
def click_event(event, x, y, flag, prama):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points)<4:
            font = cv2.FONT_HERSHEY_SIMPLEX
            strxy = '* '+str(x)+' '+str(y)
            cv2.putText(img, strxy, (x,y), font, 0.5, (0,0,255), 1, cv2.LINE_AA)        
            cv2.imshow('Track Road',img)
            points.append((x,y))
            print(f"Coordinate ({x}, {y})")
        else:
            cv2.line(img, points[0], points[1], (0,255,0), 2, cv2.LINE_AA)
            cv2.line(img, points[1], points[2], (0,255,0), 2, cv2.LINE_AA)
            cv2.line(img, points[2], points[3], (0,255,0), 2, cv2.LINE_AA)
            print("**Coordinates Saved (press 'q' to exit)**")

print(f"""╔{''.center(28,'═')}╗
║{"Procedure".center(28,' ')}║
╚{''.center(28,'═')}╝
1. Press 's' to take screen shot of road
2. select 4 coordinate on border of road (LB->LU->RU->RD)
3. press 'q' to quit screen shot screen
""")

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

while(len(points)<4):
    points.clear()
    print("Enter 4 Coordinates")
    img = cv2.imread('road_Data.jpg')
    cv2.imshow('Track Road',img)
    cv2.setMouseCallback('Track Road', click_event)
    if(cv2.waitKey(0)==ord('q')):
        cv2.destroyAllWindows()

counterLine = []
counterLine.extend(points[1:3])
