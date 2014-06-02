import minecraft as minecraft
import time
import random

mc = minecraft.Minecraft.create()

mc.player.setTilePos(0,0,0)
while True == True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x - 2,y - 2, z - 2,x + 2, y + 2,z + 2,0)
