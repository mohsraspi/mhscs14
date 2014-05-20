import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.4.16")
import time

for w in range(31):
    time.sleep(0)
    W = 30 - w
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z
    mc.setBlocks(x-W,y-1,z-W,x+W,y-1,z+W,41)
    mc.player.setTilePos(x,y+1,z)
mc.setBlock(x,y-1,z,41)
