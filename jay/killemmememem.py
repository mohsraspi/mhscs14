import minecraft as minecraft
import random
import time
import math

mc = minecraft.Minecraft.create()
mc.setBlocks(-30,0,-30,30,0,30,2)
mc.setBlocks(-30,1,-30,30,63,30,0)
while True == True:
    time.sleep(.02)

    ranz = random.randint(-10,10)
    rany = random.randint(63,63)
    ranx = random.randint(0,0)
    ranyy = random.randint(0,0)
    randwool = random.randint(1,16)
    
    mc.setBlock(ranx,rany,ranz,12)
    mc.setBlocks(0,0,0,0,63,0,0)

    



