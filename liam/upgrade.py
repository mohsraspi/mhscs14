import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(input())
import time

for x in range(-130,130):
    for z in range(-130,130):
        for y in range(-70,70):
            t = mc.getBlock(x,y,z)
            if t == 1:
                mc.setBlock(x,y,z,16)
            if t == 2:
                mc.setBlock(x,y,z,3)
            if t == 3:
                mc.setBlock(x,y,z,1)
            if t == 16:
                mc.setBlock(x,y,z,15)
            if t == 15:
                mc.setBlock(x,y,z,73)
            if t == 73:
                mc.setBlock(x,y,z,21)
            if t == 21:
                mc.setBlock(x,y,z,14)
            if t == 14:
                mc.setBlock(x,y,z,56)
            if t == 56:
                mc.setBlock(x,y,z,57)
            if t == 4:
                mc.setBlock(x,y,z,42)
            if t == 42:
                mc.setBlock(x,y,z,22)
            if t == 22:
                mc.setBlock(x,y,z,41)
            if t == 41:
                mc.setBlock(x,y,z,57)
            if t == 5:
                mc.setBlock(x,y,z,45)
            if t == 45:
                mc.setBlock(x,y,z,46,1)
