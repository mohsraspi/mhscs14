import minecraft as minecraft
mc = minecraft.Minecraft.create()

def growTree(x, y, z):
    x = 28
    y = 8
    z = 18
    blockType = 6
    mc.setBlocks(x, y, z, blockType)
    
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
