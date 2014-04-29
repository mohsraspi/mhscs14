import minecraft as minecraft
mc = minecraft.Minecraft.create('10.52.4.54')
import random
import time
mc.setBlocks(10,-64,10,-10,64,-10,0)
mc.setBlocks(10,-60,10,-10,-57,-10,7)
mc.setBlocks(10,-58,10,-10,-50,-10,12)
while True == True:
    time.sleep(.05)
    x = random.randint(-10,10)
    z = random.randint(-10,10)
    y = random.randint(-60, -55)
    mc.setBlock(x,y,z,0)
    
