import minecraft as minecraft
#mc = minecraft.Minecraft.create('10.52.3.80')#
mc = minecraft.Minecraft.create('10.52.4.54')#j
#mc = minecraft.Minecraft.create('10.52.3.139')#tom
#mc = minecraft.Minecraft.create('10.52.3.235')#steven
#mc = minecraft.Minecraft.create('10.52.2.244')#
#mc = minecraft.Minecraft.create('10.52.3.39')#arse
#mc = minecraft.Minecraft.create('10.52.5.32')#
#mc = minecraft.Minecraft.create('10.52.3.11')#
#mc = minecraft.Minecraft.create('10.52.5.30')#
#cm = minecraft.Minecraft.create('10.52.5.124')#liam
#mc = minecraft.Minecraft.create()#tobias
import random
z=25
x=25
y= input()
while y>=0:
    j= mc.getBlock(x,y,z)
    if j==2:
        k=random.randint(1,2)
        if k==1:
            mc.setBlock(x,y+1,z,37)
        if k==2:
            mc.setBlock(x,y+1,z,38)
    z=z-1
    if z <= -25:
        z=25
        x=x-1
        if x<=-25:
            x=25
            y=y-1
