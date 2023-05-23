import cv2
img=cv2.imread('solar-system.jpg')

cv2.putText(img,'Sun',(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(225,225,225))
cv2.putText(img,'Mercury',(100,150),cv2.FONT_HERSHEY_COMPLEX,0.7,(225,225,225))
cv2.putText(img,'Venus',(180,270),cv2.FONT_HERSHEY_COMPLEX,0.7,(225,225,225))
cv2.putText(img,'Earth',(300,150),cv2.FONT_HERSHEY_COMPLEX,0.7,(225,225,225))
cv2.putText(img,'Mars',(380,270),cv2.FONT_HERSHEY_COMPLEX,0.7,(225,225,225))
cv2.putText(img,'Jupiter',(540,50),cv2.FONT_HERSHEY_COMPLEX,1,(225,225,225))
cv2.putText(img,'Saturn',(700,120),cv2.FONT_HERSHEY_COMPLEX,1,(225,225,225))
cv2.putText(img,'Uranus',(900,120),cv2.FONT_HERSHEY_COMPLEX,1,(225,225,225))
cv2.putText(img,'Neptune',(1100,120),cv2.FONT_HERSHEY_COMPLEX,1,(225,225,225))
cv2.imshow('output',img)
cv2.waitKey(0)



