import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(input())
import time
import random
f = 10
while f == 10:
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z
    w = random.randint(-1,9)
    mc.setBlocks(x-2,y+2,z-2,x+2,y+2,z+2,38,w)
    time.sleep(5)
 


