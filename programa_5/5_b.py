import pdb 
import torch
from PIL import Image
import os
from torchvision import transforms
import torchvision.transforms.functional as TF


pdb.set_trace()

lista = os.listdir(".")
x = []

for i in range (len(lista)):
    m = Image.open(lista[i])
    m = TF.to_tensor(m)
    x.append(m)

x = torch.stack(x)
x.cuda
print(x.shape)

