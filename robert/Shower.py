import minecraft as minecraft
import time
import math
mc= minecraft.Minecraft.create()
mc.setBlocks(-28,4,7,-24,8,4,3)
mc.setBlocks(-27,5,6,-25,7,5,0)
mc.setBlocks(-26,5,4,-26,6,4,0)
mc.setBlocks(-26,4,6,-26,4,6,0)
while True== True:
    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z
    if x>-28 and x<-24 and y>4 and y<8 and z>4 and z<8:
        mc.setBlock(-26,8,6,8)
    if x<-28 or x>-24 or y<4 or y>8 or z<4 or z>8:
        mc.setBlock(-26,8,6,3)
    
    
