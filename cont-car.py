

import cv2 
import numpy as np
from directkeys import PressKey,ReleaseKey,W,A,S,D

import time
time.sleep(2)
def main():

    cc=cv2.VideoCapture(0)
    fram=np.zeros((300,300),'float')
    while True:
        retval,frame=cc.read()
        if retval:
            fram=frame[0:300,0:300]
            gr=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
            hsv=cv2.cvtColor(fram,cv2.COLOR_BGR2HSV)
            hsv=cv2.medianBlur(hsv,11)
            low=np.array([0,48,80])
            hi=np.array([25,255,255])
            mask=cv2.inRange(hsv,low,hi)
            blur=cv2.medianBlur(mask,5)
            _,cts,hie=cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            if len(cts)!=0:
                areas=[cv2.contourArea(i) for i in cts]     
                maxcnt=cts[np.argmax(areas)]
                hull=cv2.convexHull(maxcnt,returnPoints=False)    
                defecti=cv2.convexityDefects(maxcnt,hull)
                M=cv2.moments(maxcnt)
                if (max(areas)<4500):
                    ReleaseKey(A)
                    ReleaseKey(D)
                    PressKey(W)
                    cv2.putText(frame,'STRAIGHT',(10,50), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),2,cv2.LINE_AA) 

                else: 
                    ReleaseKey(W)
            #ReleaseKey(S)
                    try:
                        cx=int(M['m10']/M['m00'])
                        cy=int(M['m01']/M['m00'])
                        left=0
                        right=0
                        for z in range(defecti.shape[0]):                             
                            s,e,f,d = defecti[z,0] 
                            start = tuple(maxcnt[s][0]) 
                            end = tuple(maxcnt[e][0]) 
                            far = tuple(maxcnt[f][0])
                            cv2.line(frame,start,end,(0,255,0),2) 
                            if end[1]<cy:
                                if end[0]<cx:
                                    left+=1
                                elif end[0]>cx:
                                    right+=1
                                #cv2.line(frame,end,(cx,cy),(0,0,255),3)
                        if left>right:
                            ReleaseKey(A)
                            PressKey(D)
                        elif right>left:
                            ReleaseKey(D)
                            PressKey(A)
                      
                    
                        cv2.putText(frame,'RIGHT' if left>right else 'LEFT',(40,50), cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,0),2,cv2.LINE_AA) 
                        #cv2.putText(fram,str(cv2.contourArea(maxcnt)),(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)        
                        cv2.circle(fram,(cx,cy),3,(0,255,0),-1)
                    except (ZeroDivisionError and TypeError):
                        pass
            
            cv2.imshow('image',fram)
            cv2.imshow('blur', blur)
            if cv2.waitKey(2) & 0xFF==ord('q'):
                break
    cc.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()    