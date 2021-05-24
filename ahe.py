import cv2
import numpy as np
import sys
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

luvimg = cv2.cvtColor(inputImage, cv2.COLOR_BGR2LUV)

rows, cols, bands = inputImage.shape

if(bands != 3) :
    print("Input image is not a standard color image:", inputImage)
    sys.exit()

output_image=luvimg

def hist_eq(org_img,w,i,j,output_image):
    L,u,v = org_img[i, j]
    hs_eq = cv2.equalizeHist(org_img[i-w:i+w+1, j-w:j+w+1, 0])
    limit=2*w+1
    r=c=limit//2
    output_image[i,j]=hs_eq[r,c],u,v


for i in range(w, rows-w) :
    for j in range(w, cols-w):
        hist_eq(luvimg,w,i,j,output_image)

output_image = cv2.cvtColor(output_image,cv2.COLOR_Luv2BGR)
cv2.imwrite(name_output,output_image)
