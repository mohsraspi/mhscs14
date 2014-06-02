import minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create()
yus = mc.getPlayerEntityIds()
#player1 = minecraft.Minecraft.create("10.52.3.80")
#player2 = minecraft.Minecraft.create("10.52.4.54")
#player3 = minecraft.Minecraft.create("10.52.3.139")
#player4 = minecraft.Minecraft.create("10.52.3.39")
#player5 = minecraft.Minecraft.create("10.52.3.235")
#player6 = minecraft.Minecraft.create("10.52.2.244")
#player7 = minecraft.Minecraft.create("10.52.4.16")
#player8 = minecraft.Minecraft.create("10.52.4311")
#player9 = minecraft.Minecraft.create("10.52.5.124")

ranx = random.randint(110,125)
negx = random.randint(-125,-110)
ranz = random.randint(110,125)
negz = random.randint(-125,-110)

yus = mc.getPlayerEntityIds()
for i in yus:
    posistion = mc.entity.getTilePos(i)
    mc.setBlock(posistion.x,posistion.y,posistion.z)
    

def startgame():

    for i in yus:
        print(yus)
        mc.entity.setTilePos(i,0,2,0)


    mc.postToChat("warning, pre-game lag")
    mc.setBlocks(-128,0,-128,128,0,128,2)
    mc.setBlocks(-128,1,-128,128,63,128,0)

    mc.setBlocks(-128,-64,-128,-100,1,-100,0)
    mc.setBlocks(-127,1,-127,-110,5,-110,49)
    mc.setBlocks(-126,1,-126,-111,5,-111,0)
    mc.setBlocks(-127,0,-127,-110,0,-110,4)

    mc.setBlocks(128,-64,128,100,1,100,0)
    mc.setBlocks(127,1,127,110,5,110,49)
    mc.setBlocks(126,1,126,111,5,111,0)
    mc.setBlocks(127,0,127,110,0,110,4)

    mc.setBlock(negx,2,negz,57)
    mc.setBlock(ranx,2,ranz,57)
    
    mc.postToChat("these are the rules:")
    mc.postToChat("1.Choose a team (positive or negative)")
    mc.postToChat("2.Defend your block")
    mc.postToChat("3.Destroy the enemies' block")
    mc.postToChat("You may use code, as long as it does not make winning imposssible")
    mc.postToChat("The world boders")
    
startgame()

while True == True:
    for i in yus:
        pos = mc.entity.getTilePos(i)
        x = pos.x
        y = pos.y
        
        if x <= -100:
           mc.entity.setTilePos(i,pos.x,-666,pos.z)
        if y >= 64:
            mc.entity.setTilePos(i,pos.x,-666,pos.z)


    w = mc.getBlock(negx,2,negz)
    e = mc.getBlock(ranx,2,ranz)
    if w == 0:
        mc.postToChat("POSITIVE WINS")
        time.sleep(3)
        startgame()
        
    
    elif e == 0:
        mc.postToChat("NEGATIVE WINS")
        time.sleep(3)
        startgame()


