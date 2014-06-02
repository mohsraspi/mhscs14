import minecraft as minecraft
mc = minecraft.Minecraft.create()

x = -42.8
y = 48
z = -54.7
blockType = 10
mc.setBlock(x, y, z, blockType)

x = x + 1
y = y + 1
z = z + 1
mc.setBlock(x, y, z, blockType)
