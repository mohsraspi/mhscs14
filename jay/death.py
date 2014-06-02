import minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create("10.52.4.16")
yus = mc.getPlayerEntityIds()
while True == True:
    for i in yus:
        print(yus)
        mc.entity.setTilePos(i,0,-666,0)
