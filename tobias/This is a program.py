import minecraft as minecraft
mc = minecraft.Minecraft.create('10.52.4.54')
import random
x=random.randint(-120,120)
y=random.randint(5,50)
z=random.randint(-120,120)
j=0
pinput = input()
if pinput == '1' or pinput == 'blob':
    while j<=100:
        x=random.randint(-120,120)
        y=random.randint(5,50)
        z=random.randint(-120,120)
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-4,x+2,y+2,z+4,45)
        mc.setBlocks(x-4,y-2,z-2,x+4,y+2,z+2,45)
        mc.setBlocks(x-2,y-4,z-2,x+2,y+4,z+2,45)
if pinput == '2' or pinput == 'box':
    while j<=100:
        x=random.randint(-120,120)
        y=random.randint(5,50)
        z=random.randint(-120,120)
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-3,x+2,y+2,z+3,0)
        mc.setBlocks(x-3,y-2,z-2,x+3,y+2,z+2,0)
        mc.setBlocks(x-2,y-3,z-2,x+2,y+3,z+2,0)
if pinput == '3' or pinput == 'glass':
    while j<=100:
        x=random.randint(-120,120)
        y=random.randint(5,50)
        z=random.randint(-120,120)
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-3,x+2,y+2,z+3,20)
        mc.setBlocks(x-3,y-2,z-2,x+3,y+2,z+2,20)
        mc.setBlocks(x-2,y-3,z-2,x+2,y+3,z+2,20)
        mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,0)
if pinput == '4' or pinput == 'pyramid':
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


