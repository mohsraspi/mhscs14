import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

position = mc.player.getTilePos()
x= position.x
y= position.y
z= position.z
#mc.player.setTilePos(x,y+30,z)
mc.setBlocks(x-10,y-1,z-10,x+10,y+19,z+10,57)
mc.setBlocks(x-9,y,z-9,x+9,y+18,z+9,0)
mc.setBlocks(x-9,y+10,z-9,x+9,y+10,z+9,57)

mc.setBlocks(x,y,z-10,x,y+1,z-10,64)
mc.setBlocks(x,y+11,z-10,x,y+12,z-10,64)
#mc.player.setTilePos(x,y,z)
