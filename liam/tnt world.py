import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.4.54")
import time

for X in range(-13,13):
    for Z in range(-13,13):
        for Y in range(-7,7):
            x = X*10
            y = Y*10
            z = Z*10
            mc.setBlocks(x,y,z,x+10,Y+10,z+10,46,1)
