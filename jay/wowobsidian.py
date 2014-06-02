import minecraft as minecraft
import random
import time

x = 128
y = 2
z = 128
mc = minecraft.Minecraft.create()

while y < 63:

    j = mc.getBlock(x,y,z)
    if j == 0:
        mc.setBlock(x,y,z,8)


    z = z - 1
    if z <= -128:                                                                                        
        z = 128
        x = x - 1
        if x<= -128:
            x = 128
            y = y + 1
        
    

  
