import minecraft as minecraft
#mc = minecraft.Minecraft.create('10.52.4.54')
#mc = minecraft.Minecraft.create('10.52.5.124')
mc = minecraft.Minecraft.create('')
import random
import time
p=20
y=-7
n=-20
while p >= 1:
    mc.setBlocks(p,y,p,n,y,n,45)
    p = p-1
    n = n+1
    y = y+1
mc.setBlocks(2,-5,-5,-2,10,-9,45)
mc.setBlocks(1,-4,-6,-1,10,-8,0)

mc.setBlocks(2,-5,5,-2,10,9,45)
mc.setBlocks(1,-4,6,-1,10,8,0)

mc.setBlocks(2,-5,-5,2,10,-5,0)
mc.setBlocks(-2,-5,-5,-2,10,-5,0)
mc.setBlocks(2,-5,-9,2,10,-9,0)
mc.setBlocks(-2,-5,-9,-2,10,-9,0)
mc.setBlocks(2,-5,5,2,10,5,0)
mc.setBlocks(-2,-5,5,-2,10,5,0)
mc.setBlocks(2,-5,9,2,10,9,0)
mc.setBlocks(-2,-5,9,-2,10,9,0)
#------------------------------
mc.setBlocks(-5,-5,-5,5,5,5,45)
mc.setBlocks(-4,-4,-4,4,4,4,0)
mc.setBlocks(0,-4,-5,0,-3,-5,0)
mc.setBlocks(0,-4,5,0,-3,5,0)
y=-4
x=-1
while y!=64:
    x=x+1
    mc.setBlock(x,y,0,0)
    y=y+1
    mc.setBlock(x,y,0,0)
y=-3
x=-2
while y!=64:
    x=x+1
    mc.setBlock(x,y,0,0)
    y=y+1
    mc.setBlock(x,y,0,0)

j = False
while j != True:
    b=mc.player.getTilePos().x
    n=mc.player.getTilePos().y
    m=mc.player.getTilePos().z
    if b == 0 and n == -4 and m == 0:
        mc.setBlocks(2,-5,2,-2,0,-2,45)
        mc.setBlocks(1,-4,1,-1,-2,-1,0)
        j = True
while True == True:
    mc.setBlocks(2,-5,2,-2,-1,-2,45)
    mc.setBlocks(1,-4,1,-1,-2,-1,0)
    time.sleep(0.4)
