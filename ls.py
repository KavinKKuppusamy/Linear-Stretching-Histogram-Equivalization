import cv2
import numpy as np
import sys
import copy

if(len(sys.argv) != 3) :
    print(sys.argv[0], ": takes 2 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: ImageIn ImageOut.")
    print("Example:", sys.argv[0], "fruits.jpg out.png")
    sys.exit()

name_input = sys.argv[1]
name_output = sys.argv[2]

inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)

luvimg = cv2.cvtColor(inputImage, cv2.COLOR_BGR2LUV)

rows, cols, bands = inputImage.shape

if(bands != 3) :
    print("Input image is not a standard color image:", inputImage)
    sys.exit()

Luv2 = copy.deepcopy(luvimg)
L,U,V = cv2.split(luvimg)

L_val = copy.deepcopy(L)
L_val1 = np.array(L_val)


#returns the max value for linear scaling
b = max(map(max,L_val1))
#returns min value for linear scaling
a = min(map(min,L_val1))

A = 0
B = 255

for i in range(0, rows) :
    for j in range(0, cols) :
        L, u, v = luvimg[i, j]
        L2 = round(((L-a)*(B-A))/(b-a) + A)
        Luv2[i,j] = [L2,u,v]

luv_lscl_img = cv2.cvtColor(Luv2, cv2.COLOR_Luv2BGR)

cv2.imwrite(name_output,luv_lscl_img)