import minecraft as minecraft
import math
import time
import random
mc = minecraft.Minecraft.create()

tileX = random.randint(-127, 127)
tileZ = random.randint(-127, 127)
tileY = mc.getHeight(tileX, tileZ)

diamond = 57
block = diamond
mc.setBlock(tileX, tileY, tileZ, diamond)
mc.postToChat('block ready')
