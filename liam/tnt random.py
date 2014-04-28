import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.5.17")
import random
import time
r = 5
while r == 5:
    
    x = random.randint(-130,130)
    y = random.randint(-70,70)
    z = random.randint(-130,130)
    mc.setBlock(x,y,z,46,1)
