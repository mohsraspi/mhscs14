import minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
friendgame = minecraft.Minecraft.create("10.52.4.54")


#position = friendgame.player.getTilePos()
#x = position.x
#y = position.y
#z = position.z
x = 110
y = 33
z = -70
base = 5
x1 = x
x2 = x + base
z1 = z
z2 = z + base
while x2 - x1>=0:
    friendgame.setBlocks(x1,y,z1,x2,y,z2,46,1)
    x1 = x1+1
    x2 = x2 - 1
    z1 = z1+1
    z2 = z2 -1
    y = y+1
