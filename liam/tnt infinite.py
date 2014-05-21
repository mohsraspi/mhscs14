import bob.minecraft as minecraft
mc = minecraft.Minecraft.create()
import random
import time
f = []
e = 6

position = mc.player.getTilePos()
x= position.x
y= position.y
z= position.z
mc.setBlock(x,y,z,46,1)
f.append(x)
f.append(y)
f.append(z)
while e == 6:
    x = f[0]
    y = f[1]
    z = f[2]
    if mc.getBlock(x,y,z) != 46:
        mc.setBlocks(x-1,y-1,z-1,x+1,y+1,z+1,46,1)
        time.sleep(4)


