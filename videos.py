import cv2
import datetime

#cap= cv2.VideoCapture(0) : 0 for default camera of your device

cap= cv2.VideoCapture("video.avi") 

fourcc= cv2.VideoWriter_fourcc(*'XVID') #Compressed format

output = cv2.VideoWriter('Register.avi',fourcc,20.0,(640,480))
#print("Frame Widht before setting", cap.get(cv2.CAP_PROP_FRAME_WIDHT))
#print("Frame Height before setting", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame=cap.read()
    output.write(frame)
    """
    To get width and height
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    """

    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text="widht :"+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " Height :" + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        dT=datetime.datetime.now() #If you want to display date use dT instead of text.
        frame=cv2.putText(frame, text,(10,20),font,1,(0,0,255),2,cv2.LINE_AA)
        #if you want to transform to gray: gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("video frame", frame)
        
        if cv2.waitKey(1)==ord('q'):
            break

cap.release()
output.release()
cv2.destroyAllWindows()