import cv2
import torch
from torchvision import transforms

t1 = torch.tensor(1, dtype = torch.int32, device = "cuda")
t2 = torch.tensor([1.1, 2.2, 3.3], dtype = torch.double, device = "cuda")
t3 = torch.tensor([
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]
], dtype=torch.float32, device = "cuda")

ta = torch.tensor(2, dtype = torch.int32, device = "cuda")
tb = torch.tensor([4.4, 5.5, 6.6], dtype = torch.double, device = "cuda")
tc = torch.tensor([
    [4,4,4,4],
    [5,5,5,5],
    [6,6,6,6]
], dtype=torch.float32, device = "cuda")
sum1 = t1 + ta
sum2 = t2 + tb
sum3 = t3 + tc

mult1 = t1 * ta
mult2 = t2 * tb
mult3 = t3 * tc

#conca1 = torch.cat((t1,ta))
conca2 = torch.cat((t2,tb),0)
conca3 = torch.cat((t3,tc),0)

print(t1, "+", ta,"=", sum1)
print(t2 , "+" , tb ,"=" , sum2)
print(t3 , "+" , tc ,"=" , sum3)

print(t1 , "*" , ta ,"=" , mult1)
print(t2 , "*" , tb ,"=" , mult2)
print(t3 , "*" , tc ,"=" , mult3)

#print(t1 , "+" , ta ,"=" , conca1)
print(t2 , "+" , tb ,"=" , conca2)
print(t3 , "+" , tc ,"=" , conca3)
