import minecraft as minecraft
import time
import math
import random
mc=minecraft.Minecraft.create()
friendgame=minecraft.Minecraft.create("10.52.3.2")
while True == True:
    time.sleep(.002)
    ranx=random.randint(-128,128)
    rany=random.randint(-64,64)
    ranz=random.randint(-128,128)
    friendgame.setBlocks(ranx-2,rany-2,ranz-2,ranx+2,rany+2,ranz+2,0)
