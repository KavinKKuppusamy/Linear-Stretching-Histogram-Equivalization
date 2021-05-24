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

eq_L = cv2.equalizeHist(luvimg[:, :, 0])

luvimg[:, :, 0] = eq_L

new_c_img = cv2.cvtColor(luvimg, cv2.COLOR_LUV2BGR)

cv2.imwrite(name_output,new_c_img)


