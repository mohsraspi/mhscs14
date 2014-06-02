import minecraft as minecraft
import random
import time
mc = minecraft.Minecraft.create("10.52.2.213")
z = 10
x = -10
y = 0
while y > -10:                                                
    j = mc.getBlock(x,y,z)
    if j==17:
        mc.setBlock(x,y,z,45)
        mc.postToChat('17')
    if j==9:
        mc.setBlock(x,y,z,11)
        mc.postToChat('9')
    if j == 2:
        mc.setBlock(x,y,z,87)
        mc.postToChat('2')
    if j == 3:
        mc.setBlock(x,y,z,88)
        mc.postToChat('3')
    if j == 1:                                                                  
        mc.setBlock(x,y,z,49)
        mc.postToChat('1')
    if j == 12:
        mc.setBlock(x,y,z,88)
        mc.postToChat('12')
    else:
        mc.setBlock(x,y,z,0)
        mc.postToChat('0')


                                                                                                                                                                                                                                                                                
                                                                

           
