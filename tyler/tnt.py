import minecraft as minecraft
mc = minecraft.Minecraft.create()

x1 = 32.1
y1 = 0
z1 = -7.4
x2 = 27.1
y2 = 10
z2 = 62
blockType = 46, 1

mc.setBlocks(x1, y1, z1, x2, y2, z2, blockType)
