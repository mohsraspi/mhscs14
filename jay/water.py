import minecraft as minecraft
import time
import random

mc = minecraft.Minecraft.create()




while True == True:
    pos = mc.player.getTilePos()
    x = pos.x
    y= pos.y
    z = pos.z
    j = mc.getBlock(x,y,z)
    
    
    mc.setBlock(x,y,z,9)
    mc.setBlock(x,y,z,j)
