import minecraft as minecraft

mc = minecraft.Minecraft.create()

import time
import random

x = 20
y = 15
z = 50

mc.player.setTilePos(x, y, z)

time.sleep(4)

x = 6
y = 10
z = 22

mc.player.setPos(x, y, z)

x = 7
y = -5
z = -6

##
##while True == True:
##    x = x + 1
##    blockType = random.randint(1,247)
##    mc.setBlock(x, y, z, blockType)
##
##    if x > 16:
##        x = 0
##        y = y + 1
        
    
