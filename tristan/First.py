import minecraft as minecraft
mc=minecraft.Minecraft.create()
x= 45
y= 45
z= 45
mc.player.setTilePos(x,y,z)

x1 = 20
y1 = 20
z1 = 20
x2 = 44
y2 = 44
z2 = 44
blockType = 46,1
mc.setBlocks(x1, y1, z1, x2, y2, z2, blockType)
