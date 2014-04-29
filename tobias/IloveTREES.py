import minecraft as minecraft
#mc = minecraft.Minecraft.create('10.52.4.54')
mc = minecraft.Minecraft.create()
import random
import time
z=25
x=25
y= input()
while y>=0:
    j= mc.getBlock(x,y,z)
    if j==17:
        mc.setBlock(x,y,z,89)
    if j==18:
        mc.setBlock(x,y,z,103)
    if j==2:
        mc.setBlock(x,y,z,35,13)
    if j==3:
        mc.setBlock(x,y,z,35,12)
    #if j==12:
        #mc.setBlocks(x,y,z,45)
    z=z-1
    if z <= -25:
        z=25
        x=x-1
        if x<=-25:
            x=25
            y=y-1
