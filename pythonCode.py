
import face_recognition as fc
import cv2
import os
import pickle
import time

print(cv2.__version__)
fpsReport=0
scaleFactor=.5
dispW=640  
dispH=480
flip=2
Encodings=[] 
Names=[]
a=[]
b=[]
t=[]
b=[]
c=150
y=165
with open('train.pkl','rb') as f:   
    Names=pickle.load(f)
    Encodings=pickle.load(f)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
outVid=cv2.VideoWriter('video/video13.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH)) 
timeStamp=time.time()     
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame=cam.read()
    frameSmall=cv2.resize(frame,(0,0),fx=scaleFactor,fy=scaleFactor)      
    frameRGB=cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)   
    facePos= fc.face_locations(frameRGB)
    allEncodings= fc.face_encodings(frameRGB, facePos)
    for (top,right,bottom,left), FaceEncodings in zip(facePos,allEncodings):
        a.append(left)
        b.append(right)
        t.append(top)
        b.append(bottom)
        name='Unknown Person'
        x=''
        matches=fc.compare_faces(Encodings,FaceEncodings,tolerance=0.52)
        if True in matches:            
           first_match_index= matches.index(True)  
           name= Names[first_match_index]  
           #x= 'Dtected Without Mask'
        top=int(top/scaleFactor) 
        right=int(right/scaleFactor)
        bottom=int(bottom/scaleFactor)
        left=int(left/scaleFactor)
        if name!='Unknown Person':
            cv2.rectangle(frame,(left,top),(right,bottom),(0,100,255),2) #165 for orange
            cv2.putText(frame,name+', [No Mask]',(left,bottom+20),font,.60,(0,100,255),1)
    if len(a)==2:
        if a[0]<a[1]:
           c=a[1]-b[0]
           x_0=b[0]
           x_1=a[1]
           y_0=(t[0]+b[0])/2
           y_1=(t[1]+b[1])/2
        if a[1]<a[0]:
           x_0=b[1]
           x_1=a[0]
           y_0=(t[1]+b[1])/2
           y_1=(t[0]+b[0])/2
           c=a[0]-b[1]
        if c>150:
           cv2.putText(frame,'',(150,25),font,.80,(255,0,255),1)
        if c<150:

           cv2.line(frame,(x_0,y_0),(x_1,y_1),(0,0,255),4) 
           cv2.putText(frame,'Distanciation is not respected !!',(25,25),font,.80,(0,0,255),1)
           cv2.putText(frame,'in Damage',(left,top-20),font,.80,(0,0,255),2) 
    facePos=0
    a=[]
    b=[]
    t=[]
    b=[] 
    cv2.imshow('piCam',frame) 
    cv2.moveWindow('piCam',0,0)
    outVid.write(frame) 

    if cv2.waitKey(1)==ord('q'):  
        break

cam.release()
cv2.destroyAllWindows()     