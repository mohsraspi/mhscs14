import minecraft as minecraft
import time
x = 0
y = 0
z = 0
mc  = minecraft.Minecraft.create()

while True == True:
    time.sleep(.001)
    x = mc.player.getTilePos().x
    y = mc.player.getTilePos().y
    z = mc.player.getTilePos().z
    
    mc.setBlock(x,y,z,9)
    mc.setBlock(x,y,z,11)
    mc.setBlock(x,y,z,0)
                 
