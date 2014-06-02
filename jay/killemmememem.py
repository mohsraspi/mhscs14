import minecraft as minecraft
import random
import time
import math

mc = minecraft.Minecraft.create()
mc.postToChat("warning, pre-game lag")
mc.setBlocks(-128,0,-128,128,0,128,2)
mc.setBlocks(-128,1,-128,128,63,128,0)

while True == True:
    
    
    time.sleep(.02)

    ranz = random.randint(-10,10)
    rany = random.randint(63,63)
    ranx = random.randint(-10,10)
    ranyy = random.randint(0,0)
    randwool = random.randint(1,16)
    
    mc.setBlock(ranx,rany,ranz,12)
    j = mc.getBlock(ranx,0,ranz)
    if j == 50:
        mc.setBlock(ranx,0,ranz,0)
    
    
    mc.setBlocks(0,1,0,0,63,0,0)

    



    
