import minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

x = pos.x - 1
y = pos.y + 1
z = pos.z
mc.setBlock(x - 1,y,z, 46,1)
mc.setBlock(x - 2,y,z, 46,1)
mc.setBlock(x - 3,y,z, 46,1)
mc.setBlock(x - 4,y,z, 0,0)
mc.setBlock(x - 5,y,z, 0,0)
mc.setBlock(x - 6,y+1,z, 46,1)




mc.setBlock(x - 1,y-1,z, 49,1)

mc.setBlock(x,y,z,49,1)
mc.setBlock(x - 1,y,z-1, 49,1)
mc.setBlock(x - 1,y,z+1, 49,1)
mc.setBlock(x - 2,y,z-1, 49,1)
mc.setBlock(x - 2,y,z+1, 49,1)
mc.setBlock(x - 3,y,z-1, 49,1)
mc.setBlock(x - 3,y,z+1, 49,1)
mc.setBlock(x - 4,y,z-1, 49,1)
mc.setBlock(x - 4,y,z+1, 49,1)
mc.setBlock(x - 5,y,z-1, 49,1)
mc.setBlock(x - 5,y,z+1, 49,1)
mc.setBlock(x - 6,y,z-1, 49,1)
mc.setBlock(x - 6,y,z+1, 49,1)

mc.setBlock(x - 2,y-1,z, 49,1)
mc.setBlock(x - 3,y-1,z, 49,1)
mc.setBlock(x - 4,y-1,z, 49,1)
mc.setBlock(x - 5,y-1,z, 49,1)
mc.setBlock(x - 6,y-1,z, 49,1)


mc.setBlock(x - 3,y+1,z, 49,1)
mc.setBlock(x - 4,y+1,z, 49,1)
mc.setBlock(x - 5,y+1,z, 49,1)
