import minecraft as minecraft
mc = minecraft.Minecraft.create()

def growTree(x,y,z):
        mc.setTilePos(13.3,8,-6.7,LAVA_FLOWING)
        x = 13.3
        y= 8
        z = -6.7
        blockType = LAVA_FLOWING

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z) pg.31
