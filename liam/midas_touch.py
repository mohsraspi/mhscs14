import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.2.192")
import time
f = 10
while f == 10:
    time.sleep(.05)
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z

    mc.setBlock(x,y-1,z,41)


