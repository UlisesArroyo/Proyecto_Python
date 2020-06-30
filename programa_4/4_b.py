
import torch
from torchvision import transforms
from PIL import Image
import torchvision.transforms.functional as TF


#1° Tranformacion de nuestro dato numphy a un tensor
transform = transforms.Compose([
	 transforms.ToPILImage()])

 # Cargamos la imagen del disco duro
#imagen = cv2.imread("dog.jpg")
imagen = Image.open("dog.jpg")

imagen_t = TF.to_tensor(imagen)
#ancho,alto,canal = imagen.shape
canal,width,height = imagen_t.shape
 
imagen_t.cuda


imagen_t = imagen_t[:, 1:1+(height), 1:1+round(width/2)]

imagen_t.cpu


#2° Transformacion de tensor a numphy 
imagen_nueva =  transform(imagen_t)
#imagen_nueva = imagen_t.permute(1,2,0).numpy()
#imagen_nueva = (imagen_nueva * 255).round().astype(np.uint8)
imagen_nueva.show()
imagen_nueva.save("medio_perro.jpg")

cv2.imwrite('nuevo_medio_perro2.jpg', imagen_nueva)
cv2.imshow("prueba_3",imagen_nueva)
cv2.waitKey(0)
