import minecraft as minecraft
mc = minecraft.Minecraft.create()

position = mc.player.getTilePos()

x = position.x
y = position.y
z = position.z

while True == True:
    if x > 25 and x < 27 and y == 5 and z > 27 and z < 29:
        mc.setBlock(x, y + 8, z, 8)
        mc.postToChat('Ew. Water.')
    else:
        mc.setBlock(26, 13, 28, 16)
        mc.postToChat('WWWWWWHHHHHHHHHHYYYYYYYYYYYYYYY')
        
    
