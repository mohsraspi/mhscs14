import minecraft as minecraft
mc = minecraft.Minecraft.create('10.52.4.54')#j
#mc = minecraft.Minecraft.create()
import time
import random
mc.setBlocks(120,6,127,127,20,120,45)
mc.setBlocks(100,5,100,100,10,100,3)
mc.setBlocks(100,5,100,100,5,97,3)
mc.setBlocks(100,8,100,100,8,97,3)
mc.setBlocks(100,10,100,100,10,97,3)
mc.setBlock(100,5,95,3)
mc.setBlock(100,6,94,3)
mc.setBlock(100,7,93,3)
mc.setBlock(100,8,92,3)
mc.setBlock(100,7,91,3)
mc.setBlock(100,6,90,3)
mc.setBlock(100,5,89,3)
mc.setBlocks(100,5,83,100,10,83,3)
mc.setBlocks(100,10,80,100,10,85,3)
mc.setBlocks(100,10,75,100,10,78,3)
mc.setBlocks(100,8,78,100,10,78,3)
mc.setBlocks(100,8,75,100,8,78,3)
mc.setBlocks(100,8,75,100,5,75,3)
mc.setBlocks(100,5,75,100,5,78,3)
mc.setBlocks(100,10,71,100,5,71,3)
mc.setBlocks(100,8,68,100,8,71,3)
mc.setBlocks(100,10,68,100,5,68,3)
mc.setBlocks(100,5,65,100,8,65,3)
mc.setBlock(100,10,65,3)
mc.setBlocks(100,5,60,100,10,60,3)
mc.setBlocks(100,10,58,100,10,62,3)
mc.setBlocks(90,1,127,75,5,106,49)
mc.setBlocks(89,2,126,76,5,107,0)
mc.setBlocks(101,0,127,101,64,-127,35,3)
mc.setBlock(87,2,121,57)
mc.setBlocks(90,1,127,75,1,106,4)
mc.setBlocks(111,1,127,127,3,111,57)
mc.setBlocks(2,-5,-5,-2,10,-9,45)
mc.setBlocks(1,-4,-6,-1,10,-8,0)
j=0
while j<=100:
    x=random.randint(-120,120)
    y=random.randint(5,50)
    z=random.randint(-120,120)
    j=j+1
    mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
    mc.setBlocks(x-2,y-2,z-4,x+2,y+2,z+4,45)
    mc.setBlocks(x-4,y-2,z-2,x+4,y+2,z+2,45)
    mc.setBlocks(x-2,y-4,z-2,x+2,y+4,z+2,45)
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
#mc.player.setTilePos(0,0,0)
def stair():
    x=0
    y=0
    while y!=64:
        x=x+1
        mc.setBlock(x,y,0,45)
        y=y+1
        mc.setBlock(x,y,0,45)




x=0
y=-5
m=3
while y!=64:
    x=x+1
    mc.setBlock(x,y,0,45)
    y=y+1
    mc.setBlock(x,y,0,45)
    if m<=10:
        m=m+1
    else:
        m=0
        b=y
        while b!=-20:
            b=b-1
            mc.setBlock(x,b,0,45)
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



while True==True:
    mc.setBlocks(111,3,127,127,5,111,30)
    mc.setBlocks(111,1,127,127,0,111,30)
    mc.setBlocks(111,6,127,127,6,111,45)
