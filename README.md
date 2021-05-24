# Linear-Stretching-Histogram-Equivalization
Implementation of Linear Scaling, Histogram Equalization, Adaptive linear stretching  and Adaptive histogram equalization

## Linear stretching (ls.py)
The output is computed from the input by linearly stretching the L values in the Luv color space to their fullest range. 

## Histogram Equalization (he.py)

The output is computed from the input by histogram equalization applied only to the L values in the Luv color space.
  
## Adaptive Linear Stretching (als.py)

It gets as input a window parameter w and names of the input and the output images. The output is computed from the input by changing only the L values. The output L(i; j) is
computed by applying linear stretching to the window of size (2w+1 X  2w+1) centered at i; j. The L value at the center of the window is the output value L(i; j). 
  
## Adaptive Histogram Equalization (ahe.py)  

It gets as input a window parameter w and names of the input and the output images. The output is computed from the input by changing only the L values. The output L(i; j)
is computed by applying histogram equalization to the window of size (2w+12w+1) centered at i; j. The L value at the center of the window is the output value L(i; j). 

Execution Steps:
  python3 program(eg., ls.py) [w] inputimage outputimage
  
  [w] - only for ALS and AHE
  
  
