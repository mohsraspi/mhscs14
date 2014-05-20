import minecraft as minecraft
import time
mc=minecraft.Minecraft.create()
friendgame = minecraft.Minecraft.create("10.52.3.80")

f = 10
while f==10:
    position=friendgame.player.getTilePos()
    x=position.x
    y=position.y
    z=position.z
    mc.player.setTilePos(x,y-9,z)

    friendgame.setBlocks(x+1 ,y-4,z+1 ,x-1 ,y +3 ,z-1 ,1)
    friendgame.setBlocks(x ,y-10,z ,x ,y +2 ,z ,0)
    time.sleep(1)
