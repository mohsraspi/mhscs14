import minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create("10.52.2.248")

while True == True:
    ranx = random.randint(-128,128)
    ranz = random.randint(-128,128)
    rany = random.randint(-5,63)
    ranblk = random.randint(0,100)
    mc.setBlock(ranx,rany,ranz,ranblk)
    time.sleep(.001)
