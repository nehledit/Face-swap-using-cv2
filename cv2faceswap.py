import cv2
import time as t
v=cv2.VideoCapture(0)
b=0
fd=cv2.CascadeClassifier(r'C:\Users\hp\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
while True:
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j)
    X=[]
    Y=[]
    W=[]
    H=[]
    for (x,y,w,h) in f:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),3)
        
        X.append(x)
        Y.append(y)
        W.append(w)
        H.append(h)
        
    if(len(X)==2):
        
        t=i[Y[0]:Y[0]+min(H),X[0]:X[0]+min(W),:].copy()
        
        i[Y[0]:Y[0]+min(H),X[0]:X[0]+min(W),:]=i[Y[1]:Y[1]+min(H),X[1]:X[1]+min(W),:].copy()
        i[Y[1]:Y[1]+min(H),X[1]:X[1]+min(W),:]=t.copy()
        
    
    print(r)
    
    cv2.imshow('img',i)    
    k=cv2.waitKey(1)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        v.release()
        break    
    

        
##    l=cv2.add(i,b)
##    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
##    r,g=cv2.threshold(j,127,255,0)
##    cv2.imshow('black',d)
##    cv2.imshow('digital',g)
##    cv2.imshow('gray',j)
##Project- Multi object detection system-10
##If you get 2 or more than 2 faces swap them
##you can figure if youve touched your face on the basis of length of face then after detecting if yuor face has been detected then play a song
##        face-play
##        no-pause
##        width-volume
##    install library - python-vlc
##    pygame- model mixer

    
