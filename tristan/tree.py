import minecraft as minecraft
mc = minecraft.Minecraft.create()

def growTree(x,y,z):

    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x, y, z)
growTree(x + 1, y, z)
