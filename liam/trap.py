import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(input())
import time
w =6
position = mc.player.getTilePos()
x= position.x
y= position.y
z= position.z
mc.setting("world_immutable", False)
while w ==6:
    mc.setBlocks(x-10,y-1,z-10,x+10,y+10,z+10,57)
    mc.setBlocks(x-5,y,z-5,x+5,y+5,z+5,0)
    mc.setting("world_immutable", False)
mc.setBlocks(x-10,y-1,z-10,x+10,y+10,z+10,57)
mc.setBlocks(x-5,y,z-5,x+5,y+5,z+5,0)




