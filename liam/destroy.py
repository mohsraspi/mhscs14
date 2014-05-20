import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
e=2
position = mc.player.getTilePos()
x= position.x
y= position.y
z= position.z
while e ==2:
    
    mc.setBlocks(x-10,y-10,z-10,x+10,y+10,z+10,0)
