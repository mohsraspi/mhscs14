import minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create()

input()

call = input()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

def fire():
    while mc.getBlock(x,y,z) == 0:
        x = x + 1

    mc.setBlocks(x,y+10,z+10,x+20,y-10,z-10,0)


    
if str(input()) == "F":
    fire()
w
