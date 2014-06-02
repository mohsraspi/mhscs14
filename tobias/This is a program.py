import minecraft as minecraft
#mc = minecraft.Minecraft.create('10.52.4.54')
#mc = minecraft.Minecraft.create('10.52.2.248')
#mc = minecraft.Minecraft.create('10.52.5.124')#liam
mc = minecraft.Minecraft.create()
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
if pinput == '5' or pinput == 'web':
    while j<=100:
        x=random.randint(-120,120)
        y=random.randint(5,50)
        z=random.randint(-120,120)
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-4,x+2,y+2,z+4,30)
        mc.setBlocks(x-4,y-2,z-2,x+4,y+2,z+2,30)
        mc.setBlocks(x-2,y-4,z-2,x+2,y+4,z+2,30)
if pinput == '6' or pinput == 'war':
    while j<=500:
        x=random.randint(-120,120)
        y=random.randint(-15,50)
        z=random.randint(-120,120)
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-4,x+2,y+2,z+4,45)
        mc.setBlocks(x-4,y-2,z-2,x+4,y+2,z+2,45)
        mc.setBlocks(x-2,y-4,z-2,x+2,y+4,z+2,45)
        mc.setBlocks(x,y,z-4,x,y,z+4,46,1)
        mc.setBlocks(x,y-4,z,x,y+4,z,46,1)
        mc.setBlocks(x-4,y,z,x+4,y,z,46,1)
if pinput == '7' or pinput == 'jars':
    while j<=100:
        x=random.randint(-120,120)
        y=random.randint(5,50)
        z=random.randint(-120,120)
        r=random.randint(1,4)
        if r==2:
            bi=10
        else:
            bi=8
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-3,x+2,y+2,z+3,20)
        mc.setBlocks(x-3,y-2,z-2,x+3,y+2,z+2,20)
        mc.setBlocks(x-2,y-3,z-2,x+2,y+3,z+2,20)
        mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,bi)
        mc.setBlock(x,y+3,z,0)
if pinput == '8' or pinput == 'ores':
    while j<=100:
        x=random.randint(-120,120)
        y=random.randint(5,50)
        z=random.randint(-120,120)
        j=j+1
        mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,45)
        mc.setBlocks(x-2,y-2,z-4,x+2,y+2,z+4,45)
        mc.setBlocks(x-4,y-2,z-2,x+4,y+2,z+2,45)
        mc.setBlocks(x-2,y-4,z-2,x+2,y+4,z+2,45)
        ore=random.randint(1,15)
        if ore==1:
            mc.setBlock(x,y,z,56)
                                                                                                                if ore==2:
            mc.setBlock(x,y,z,14)
        if ore==3 or ore==4:
            mc.setBlock(x,y,z,15)
        if ore==5 or ore==6:
            mc.setBlock(x,y,z,16)
        if ore==7 or ore==8:
            mc.setBlock(x,y,z,21)
        if ore==9 or ore==10:
            mc.setBlock(x,y,z,73)
        
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


