import bob.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.4.54")
import time
##mc.player.setTilePos(0,20,0)
f = 10
while f == 10:
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z
    mc.setBlocks(x-20,y+5,z-20,x+20,y+13,z+10,12)
    time.sleep(3)
 
