import cv2
import numpy as np	
imagen_bgr = cv2.imread('colores.jpg')


imagen_rgb = cv2.cvtColor(imagen_bgr,cv2.COLOR_BGR2RGB)




RG = np.copy(imagen_rgb)
RG [:,:,2] = 0;


RB = np.copy(imagen_rgb)
RB [:,:,1] = 0;


GB = np.copy(imagen_rgb)
GB [:,:,0] = 0;



C1 = imagen_rgb[:,:,0]
C2 = imagen_rgb[:,:,1]
C3 = imagen_rgb[:,:,2]



imagen_rgb = cv2.cvtColor(imagen_bgr,cv2.COLOR_RGB2BGR)
RG = cv2.cvtColor(RG,cv2.COLOR_RGB2BGR)
RB = cv2.cvtColor(RB,cv2.COLOR_RGB2BGR)
GB = cv2.cvtColor(GB,cv2.COLOR_RGB2BGR)
C1 = cv2.cvtColor(C1,cv2.COLOR_RGB2BGR)
C2 = cv2.cvtColor(C2,cv2.COLOR_RGB2BGR)
C3 = cv2.cvtColor(C3,cv2.COLOR_RGB2BGR)




cv2.imshow("RGB", imagen_bgr)
cv2.imshow('R',C1)
cv2.imshow('G',C2)
cv2.imshow('B',C3)
cv2.imshow('RG',RG)
cv2.imshow('RB',RB)
cv2.imshow('GB',GB)

cv2.imwrite('R.jpg', C1)
cv2.imwrite('G.jpg', C2)
cv2.imwrite('B.jpg', C3)
cv2.imwrite('RG.jpg', RG)
cv2.imwrite('RB.jpg', RB)
cv2.imwrite('GB.jpg', GB)


cv2.waitKey(0)
cv2.destroyAllWindows()
