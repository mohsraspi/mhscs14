import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
f = 10
while f == 10:
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z

    mc.setBlocks(x-3,y-2,z-3,x+3,y-2,z+3,46,1)
    mc.setBlock(x,y-1,z,46,1)
    time.sleep(60)
 
