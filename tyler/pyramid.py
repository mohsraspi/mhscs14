import minecraft as minecraft
mc = minecraft.Minecraft.create()
blockType = 12
position=mc.player.getTilePos()
x=position.x
y=position.y
z=position.z
base = 20
x1 = x
x2 = x + base
z1 = z
z2 = z + base
while x2 - x1 >= 0:
    
    mc.setBlocks(x1, y, z1, x2, y, z2, blockType)
    x1 = x1 + 1
    x2 = x2 - 1
    z1 = z1 + 1
    z2 = z2 - 1
    y = y + 1
