import minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create()

mc.setBlocks(50,0,50,-50,63,-50,49)
mc.setBlocks(5,20,5,-5,30,-5,0)
mc.player.setTilePos(0,25,0)


mc.setBlock(5,20,-5,89)
mc.setBlock(-5,20,5,89)
mc.setBlock(5,20,5,89)
mc.setBlock(-5,20,-5,89)
mc.setBlock(5,30,-5,89)
mc.setBlock(-5,30,5,89)
mc.setBlock(5,30,5,89)
mc.setBlock(-5,30,-5,89)

ranx = 5

rany = random.randint(20,30)
ranchoose = random.randint(1,2)

if ranchoose == 1:
    ranx = -6

if ranchoose == 2:
    ranx = 6

mc.setBlocks(3,rany,ranx,3,rany-1,ranx,0)

while True == True:
    
    ranchoose = random.randint(1,2)
    if ranchoose == 1:
        x = x + 1

    if ranchoose == 2:
        z = z + 1
    
    mc.setBlocks(x,y,z,x1,y1,z1,0)
