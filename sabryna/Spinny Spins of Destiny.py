import minecraft as minecraft
mc = minecraft.Minecraft.create()

import time

position = mc.player.getTilePos()

x = 20
y = 15
z = 38

states = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def spinnySpinsOfDestiny():
    while True == True:
        for state in states:
            mc.setBlock(x, y + 1, z, 68, state)
            mc.setBlock(x + 2, y + 1, z, 68, state)
            mc.setBlock(x, y + 1, z + 2, 68, state)
            mc.setBlock(x + 2, y + 1, z + 2, 68, state)            
            time.sleep(0.1)
        for state in states:
            mc.setBlock(x, y, z, 35, state)
            mc.setBlock(x + 2, y, z, 35, state)
            mc.setBlock(x, y, z + 2, 35, state)
            mc.setBlock(x + 2, y, z + 2, 35, state)            
            time.sleep(0.1)

##def rouletteOfColorification():
##    while True == True:
##        for state in states:
##            mc.setBlock(x, y, z, 46, state)
##            mc.setBlock(x + 2, y, z, 46, state)
##            mc.setBlock(x, y, z + 2, 46, state)
##            mc.setBlock(x + 2, y, z + 2, 46, state)            
##            time.sleep(0.1)

spinnySpinsOfDestiny()
##rouletteOfColorification()

