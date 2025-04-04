import util
from tifffile import imread
import numpy as np
import matplotlib.pyplot as plt


# LM
fn='/Users/davis.perez/Desktop/Resliced.tif'
RL=imread(fn)

x,y,z=[469,692,110]
# x,y,z=[378,664,128]

xr,yr,zr=util.hole_fitting_RL(RL,x,y,z,show=True)

print(x,y,z)
print(xr,yr,zr)

# FIB
fn='/Users/davis.perez/Desktop/ref_MillPolishing_final_high_res_ib.tif'
im=imread(fn)
x,y=[460,555]

xr,yr=util.hole_fitting_FIB(im,x,y,show=True)
print(x,y)
print(xr,yr)

print('success')