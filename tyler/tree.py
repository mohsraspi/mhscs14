import minecraft as minecraft
mc = minecraft.Minecraft.create()

def growTree(x,y,z):

    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z
    mc.setBlocks();
growTree(x + 1, y, z)
