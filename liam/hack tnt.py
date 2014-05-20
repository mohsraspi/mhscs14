import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(input())
import time
f = 10
while f == 10:
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z

    mc.setBlocks(x-5,y-5,z-5,x+5,y+5,z+5,46,1)
    mc.setBlock(x-2,y-2,z-2,x+2,y+2,z+2,0)
    time.sleep(60)
 

