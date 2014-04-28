import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.2.192")
import time
mc.player.setTilePos(0,20,0)
f = 10
while f == 10:
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z
    mc.setBlocks(x-7,y+10,z-7,x+7,y+11,z+7,12)
    time.sleep(3)
 
