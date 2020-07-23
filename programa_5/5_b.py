"""
import pdb 
import torch
from PIL import Image
import os
from torchvision import transforms
import torchvision.transforms.functional as TF
import torch.utils.data as data
"""
#pdb.set_trace()

import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.utils.data as data
import torchvision
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
    transforms.ToTensor()])

lista = os.listdir(".")

m = torch.tensor(0, dtype = torch.int32, device = "cuda")

for i in range (len(lista)):
    n = Image.open(lista[i])
    m = transform(n)
    
    m = m[None, ::]
    if i == 0 :
        t_batch = m
        t_batch.cuda
    else :
        t_batch = torch.cat((t_batch, m), dim = 0)

print(t_batch.shape)


#
#dir = "./1CM1_1_R_#217/"
#train_data = datasets.ImageFolder(root=dir, transform=transform)
#m.cuda


"""
lista = os.listdir(".")
dir = "./1CM1_1_R_#217/"
train_data = datasets.ImageFolder(root=dir, transform=transform)
m=[]
m.cuda
for i in range (len(lista)):
    n = Image.open(lista[i])
    m = transform(n)
    
    m = m[None, ::]
    if i == 0 :
        t_batch = m
        t_batch.cuda
    else :
        t_batch = torch.cat((t_batch, m), dim = 0)

print(t_batch.shape)
"""
