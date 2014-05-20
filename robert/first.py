import minecraft as minecraft
import time
mc=minecraft.Minecraft.create()
x=11
y=-62
z=-49
#mc.player.setTilePos(x,y,z)
time.sleep(5)
mc.setBlocks(-200,63,200,200,-63,-200,0)
mc.setBlocks(-200,-63,200,200,-63,-200,2)


friendgame = minecraft.Minecraft.create("10.52.3.80")

f = 10
while f==10:
    position=friendgame.player.getTilePos()
    x=position.x
    y=position.y
    z=position.z
    mc.player.setTilePos(x,y,z)

    friendgame.setBlocks(x+1 ,y-4,z+1 ,x-1 ,y -1 ,z-1 ,0)
    
#friendgame.player.setTilePos(16,16,16)
