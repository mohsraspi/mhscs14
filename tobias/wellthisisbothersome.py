import minecraft as minecraft
#This program was made by Tobias Kipps
print('This is a program that can run a variety of funtions')
print('Enter IP')
ipo=input()
mc=minecraft.Minecraft.create(ipo)
print('Enter Second IP (only used in some programs)')
ipt=input()
if ipt != '':
    cm=minecraft.Minecraft.create(ipt)
import random
import time
j=False
x=mc.player.getTilePos().x
y=mc.player.getTilePos().y
z=mc.player.getTilePos().z
print('Enter name or ID of program you wish to run')
pinput=input()
if pinput=='web' or pinput =='1':
    mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,20)
    while mc.getBlock(x,y+1,z)==20 and mc.getBlock(x,y,z)==20 and mc.getBlock(x+1,y+1,z)==20 and mc.getBlock(x,y+1,z+1)==20 and mc.getBlock(x,y+1,z-1)==20 and mc.getBlock(x-1,y+1,z)==20:
        #ye~
        j=True
    mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,30)
if pinput=='diamond' or pinput=='2':
    mc.setBlock(x+2,y+1,z-1,57)
    #mc.setBlock(x+2,y+1,z-1,30)
    while mc.getBlock(x+2,y+1,z-1)==57:
        j=True
    x=x+2
    y=y+1
    z=z-1
    mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,30)
if pinput=='random' or pinput=='3':
    bi=random.randint(1,49)
    mc.setBlock(x+2,y+1,z-1,bi)
    while mc.getBlock(x+2,y+1,z-1)==bi:
        j=True
    x=x+2
    y=y+1
    z=z-1
    mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,30)
if pinput=='mirror' or pinput=='4':
    while True==True:
        x=mc.player.getTilePos().x
        y=mc.player.getTilePos().y
        z=mc.player.getTilePos().z
        mc.setBlock(-1*x,y,z,103)
        mc.setBlock(-1*x,y+1,z,103)
        while x==mc.player.getTilePos().x and y==mc.player.getTilePos().y and z==mc.player.getTilePos().z:
            j=False
        mc.setBlock(-1*x,y,z,0)
        mc.setBlock(-1*x,y+1,z,0)
if pinput=='mind control' or pinput=='5':
    while True==True:
      x=mc.player.getTilePos().x
      y=mc.player.getTilePos().y
      z=mc.player.getTilePos().z
      cm.player.setTilePos(x,y,z)
if pinput=='drone' or pinput=='6':
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    bi=cm.getBlock(x,y+1,z)
    g=cm.player.getTilePos().x
    h=cm.player.getTilePos().y
    j=cm.player.getTilePos().z
    bl=cm.getBlock(g,h+1,j)
    while True==True:
        b=x
        n=y
        m=z
        ni=bi
        x=mc.player.getTilePos().x
        y=mc.player.getTilePos().y
        z=mc.player.getTilePos().z
        bi=cm.getBlock(x,y+1,z)
        if bi == 103:
            bi=ni
        cm.setBlock(x,y+1,z,103)
        cm.setBlock(b,n+1,m,ni)
        u=g
        i=h
        o=j
        nl=bl
        g=cm.player.getTilePos().x
        h=cm.player.getTilePos().y
        j=cm.player.getTilePos().z
        bl=mc.getBlock(g,h+1,j)
        if bl == 103:
            bl=nl
        mc.setBlock(g,h+1,j,103)
        mc.setBlock(u,i+1,o,nl)
if pinput =='creeper' or pinput=='7':
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    b=x
    n=y
    m=z
    while True==True:
        x=mc.player.getTilePos().x
        y=mc.player.getTilePos().y
        z=mc.player.getTilePos().z
        mc.setBlocks(b-10,n-5,m-5,b-10,n+5,m+5,0)
        mc.setBlocks(x-10,y-5,z-5,x-10,y+5,z+5,103)
        mc.setBlocks(x-10,y+1,z-4,x-10,y+4,z-2,49)
        mc.setBlocks(x-10,y+1,z+4,x-10,y+4,z+2,49)
        mc.setBlocks(x-10,y-2,z-4,x-10,y-2,z+4,49)
        mc.setBlocks(x-10,y-3,z-4,x-10,y-3,z-5,49)
        mc.setBlocks(x-10,y-3,z+4,x-10,y-3,z+5,49)
        b=x
        n=y
        m=z
        time.sleep(0.8)
if pinput=='tnt' or pinput=='8':
    #mc.setBlock(x+2,y+1,z-1,57)
    mc.setBlock(x+2,y+1,z-1,46,1)
    while mc.getBlock(x+2,y+1,z-1)==46:
        j=True
    x=x+2
    y=y+1
    z=z-1
    mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,46,1)
if pinput=='grid' or pinput=='8':
    #mc.setBlock(x+2,y+1,z-1,57)
    mc.setBlock(x+2,y+1,z-1,46,1)
    while mc.getBlock(x+2,y+1,z-1)==46:
        j=True
    x=x+2
    y=y+1
    z=z-1
    time.sleep(2.5)
    mc.setBlocks(x-100,y,z,x+100,y,z,46,1)
    mc.setBlocks(x,y-100,z,x,y+20,z,46,1)
    mc.setBlocks(x,y,z-100,x,y,z+100,46,1)
    mc.setBlocks(x-100,y-1,z,x+100,y-1,z,5)
    mc.setBlocks(x,y-1,z-100,x,y-1,z+100,5)
if pinput=='eat' or pinput=='9':
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    mc.setBlocks(x,y+5,z,x,y+10,z,3)
    mc.setBlocks(x,y+5,z,x,y+5,z-3,3)
    mc.setBlocks(x,y+8,z,x,y+8,z-3,3)
    mc.setBlocks(x,y+10,z,x,y+10,z-3,3)
    mc.setBlock(x,y+5,z-5,3)
    mc.setBlock(x,y+6,z-6,3)
    mc.setBlock(x,y+7,z-7,3)
    mc.setBlock(x,y+8,z-8,3)
    mc.setBlock(x,y+7,z-9,3)
    mc.setBlock(x,y+6,z-10,3)
    mc.setBlock(x,y+5,z-11,3)
    mc.setBlocks(x,y+5,z-17,x,y+10,z-17,3)
    mc.setBlocks(x,y+10,z-20,x,y+10,z-15,3)
    mc.setBlocks(x,y+10,z-25,x,y+10,z-22,3)
    mc.setBlocks(x,y+8,z-22,x,y+10,z-22,3)
    mc.setBlocks(x,y+8,z-25,x,y+8,z-22,3)
    mc.setBlocks(x,y+8,z-25,x,y+5,z-25,3)
    mc.setBlocks(x,y+5,z-25,x,y+5,z-22,3)
    mc.setBlocks(x,y+10,z-29,x,y+5,z-29,3)
    mc.setBlocks(x,y+8,z-32,x,y+8,z-29,3)
    mc.setBlocks(x,y+10,z-32,x,y+5,z-32,3)
    mc.setBlocks(x,y+5,z-35,x,y+8,z-35,3)
    mc.setBlock(x,y+10,z-35,3)
    mc.setBlocks(x,y+5,z-40,x,y+10,z-40,3)
    mc.setBlocks(x,y+10,z-42,x,y+10,z-38,3)
if pinput=='spread' or pinput=='10':
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    j=0
    while j <=15:
        mc.setBlocks(x-j,y-j,z-j,x+j,y+j,z+j,45)
        time.sleep(5)
        j=j+1
if pinput == 'cannon' or pinput=='11':
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    mc.setBlocks(x+4,y-1,z,x+1,y-1,z,49)
    mc.setBlock(x+4,y,z,49)
    mc.setBlocks(x+3,y,z,x+1,y,z,46,1)
    mc.setBlock(x+4,y+1,z,46,1)
    mc.setBlock(x+5,y+2,z,46,1)
    mc.setBlock(x+6,y+3,z,46,1)
    mc.setBlock(x+5,y+1,z,49)
if True==False:
    z=z+1
    mc.setBlocks(x+4,y-1,z,x+1,y-1,z,49)
    mc.setBlock(x+4,y,z,49)
    mc.setBlocks(x+3,y,z,x+1,y,z,46,1)
    mc.setBlock(x+4,y+1,z,46,1)
    mc.setBlock(x+5,y+2,z,46,1)
    mc.setBlock(x+6,y+3,z,46,1)
    mc.setBlock(x+5,y+1,z,49)
    z=z+1
    mc.setBlocks(x+4,y-1,z,x+1,y-1,z,49)
    mc.setBlock(x+4,y,z,49)
    mc.setBlocks(x+3,y,z,x+1,y,z,46,1)
    mc.setBlock(x+4,y+1,z,46,1)
    mc.setBlock(x+5,y+2,z,46,1)
    mc.setBlock(x+6,y+3,z,46,1)
    mc.setBlock(x+5,y+1,z,49)
if pinput=='bedrock':
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    mc.setBlocks(x-5,y-5,z-5,x+5,y+5,z+5,7)
if pinput=='follow' or pinput=='12':
    e=mc.player.getTilePos().x
    r=mc.player.getTilePos().y
    t=mc.player.getTilePos().z
    x=0
    y=9
    z=0
    while e!=x or r!=y or t!=z:
        mc.setBlocks(x-1,y,z-1,x+1,y+2,z+1,7)
        if e > x:
            x=x+1
        if e < x:
            x=x-1
        if r > y:
            y=y+1
        if r < y:
            y=y-1
        if t > z:
            z=z+1
        if t < z:
            z=z-1
        time.sleep(.2345)
        e=mc.player.getTilePos().x
        r=mc.player.getTilePos().y
        t=mc.player.getTilePos().z
    mc.setBlocks(x-2,y-1,z-2,x+2,y+3,z+2,45)
    mc.player.setTilePos(0,-666,0)
if pinput=='follow2' or pinput=='13':
    e=mc.player.getTilePos().x
    r=mc.player.getTilePos().y
    t=mc.player.getTilePos().z
    x=0
    y=9
    z=0
    while e!=x or r!=y or t!=z:
        mc.setBlocks(x-1,y,z-1,x+1,y+2,z+1,7)
        if abs(e-x)>abs(r-y) and abs(e-x)>abs(t-z):
            if e > x:
                x=x+1
            if e < x:
                x=x-1
        elif abs(r-y)>abs(e-x) and abs(r-y)>abs(t-z):
            if r > y:
                y=y+1
            if r < y:
                y=y-1
        elif abs(t-z)>abs(r-y) and abs(t-z)>abs(e-x):
            if t > z:
                z=z+1
            if t < z:
                z=z-1
        else:
            if e > x:
                x=x+1
            if e < x:
                x=x-1
            if r > y:
                y=y+1
            if r < y:
                y=y-1
            if t > z:
                z=z+1
            if t < z:
                z=z-1
        time.sleep(.1)
        e=mc.player.getTilePos().x
        r=mc.player.getTilePos().y
        t=mc.player.getTilePos().z
    mc.setBlocks(x-2,y-1,z-2,x+2,y+3,z+2,45)
    mc.player.setTilePos(0,-666,0)
if pinput=='flood' or pinput=='14':
    x=-30
    y=0
    z=-30
    while y<=50:
        j= mc.getBlock(x,y,z)
        if j==0:
            mc.setBlock(x,y,z,8)
        z=z+1
        if z >= 30:
            z=-30
            x=x+1
            if x>=30:
                x=-30
                y=y+1
     
