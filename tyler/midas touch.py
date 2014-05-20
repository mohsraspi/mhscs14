import minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
f = 10
while f == 10:
    time.sleep(.05)
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z
    mc.setBlock(x,y-1,z,46,1)
