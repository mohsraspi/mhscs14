import minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
base = 1000
x1 = x
x2 = x + base
z1 = z
z2 = z + base
blockType = 8, 1
while x2 - x1 >= 0:
    mc.setBlocks(x1, y, z1, x2, y, z2, blockType)
    x1 = x1 + 1
    x2 = x2 - 1
    z1 = z1 + 1
    z2 = z2 - 1
    y = y + 1
