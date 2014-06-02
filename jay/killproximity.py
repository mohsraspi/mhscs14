import minecraft as minecraft
import time
import random

mc = minecraft.Minecraft.create()

yus = mc.getPlayerEntityIds()

while True == True:
    for i in yus:
        pos = mc.entity.getTilePos(i)
        x = pos.x
        y = pos.y
        
        if y <= -10:
            mc.entity.setTilePos(i,pos.x,-666,pos.z)
            mc.postToChat("player " + str(i) + " was slain buy tjufan12")
            time.sleep(2)
                          
        if y >= 10:
            mc.entity.setTilePos(i,pos.x,-666,pos.z)
            mc.postToChat("player " + str(i) + " was slain bu tjufan12")
            time.sleep(2)



