import bob.minecraft as minecraft
mc = minecraft.Minecraft.create()
import random
import time
f = []
e = 6
print(mc.getBlocks(-20,-10,-20,20,30,20))
f = mc.getBlocks(-20,-10,-20,20,30,20)
print(f)

while e == 6:
    if mc.getBlocks(-120,-60,-120,120,60,120) != f:
        position = mc.player.getTilePos()
        x= position.x
        y= position.y
        z= position.z
        mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,46,1)
        time.sleep(10)
        break
