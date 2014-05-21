import bob.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.2.176")

import random
import time
l = mc.getPlayerEntityIds()
f = []
e = 6
print(l)
while e == 6:
    for i in l:
        position = mc.entity.getTilePos(i)
        x= position.x
        y= position.y
        z= position.z
        mc.setBlock(x,y,z,46,1)
        f.append([x,y,z])
        print(f)
    
    for q in range(200):
        if len(f) !=0:
            for w in range(len(f)):
                x = f[w][0]
                y = f[w][1]
                z = f[w][2]
                if mc.getBlock(x,y,z) != 46:
                    mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,46,1)
                    del(f[w])
                    print(f)
                    time.sleep(0)
                    break
        else:
            time.sleep(.01)
    
