import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()



for x in range(15):
    position = mc.player.getTilePos()
    x= position.x
    y= position.y
    z= position.z

    mc.setBlock(x,y,z,1)

    mc.player.setTilePos(x,y+1,z)


