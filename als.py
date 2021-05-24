import cv2
import numpy as np
import sys
import math
import copy

if(len(sys.argv) != 4) :
    print(sys.argv[0], ": takes 3 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: ImageIn ImageOut.")
    print("Example:", sys.argv[0], "fruits.jpg out.png")
    sys.exit()

w = int(sys.argv[1])
name_input = sys.argv[2]
name_output = sys.argv[3]

inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)
luv_image = cv2.cvtColor(inputImage, cv2.COLOR_BGR2LUV)
rows, cols, bands = luv_image.shape
if(bands != 3) :
    print("Input image is not a standard color image:", inputImage)
    sys.exit()


A = 0
B = 255
output_luv_image=luv_image

def min_max_window(luv_image,w,i,j):
    min_pv,max_pv = float('inf'),float('-inf')
    for r in range(i-w,i+w+1):
        for c in range(j-w,j+w+1):
            L,u,v= luv_image[r,c]
            if L<min_pv:
                min_pv=L
            if L>max_pv:
                max_pv=L
    return min_pv,max_pv

for i in range(w, rows-w):
    for j in range(w, cols-w):
        min_v,max_v=min_max_window(luv_image, w, i, j)
        L,u,v = luv_image[i, j]
        mult_val = 255/max_v-min_v
        l_new = (L-min_v)*mult_val
        output_luv_image[i,j]= [l_new,u,v]

luv_lscl_img = cv2.cvtColor(output_luv_image,cv2.COLOR_Luv2BGR)
cv2.imwrite(name_output,luv_lscl_img)
