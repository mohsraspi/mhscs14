import minecraft as minecraft

mc = minecraft.Minecraft.create()

import time

x = 11
y = 11
z = 12

mc.player.setTilePos(x, y, z)

time.sleep(4)

while True:
    y = 12
    z = 13
    blockType = 103
    
    mc.setBlock(x, y, z, blockType)

    y = y + 1
    mc.setBlock(x, y, z, blockType)
