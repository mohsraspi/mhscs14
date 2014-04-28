import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

y = 1
for x in range(30):
    mc.setBlock(6,1,36,y)
    y+=1

mc.player.setTilePos(6,36,28)

