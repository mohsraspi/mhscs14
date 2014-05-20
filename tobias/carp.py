import minecraft as minecraft
#mc = minecraft.Minecraft.create('10.52.3.80')#

#cm = minecraft.Minecraft.create('10.52.4.54')#j
#mc = minecraft.Minecraft.create('10.52.3.139')#tom
#mc = minecraft.Minecraft.create('10.52.3.235')#steven
#mc = minecraft.Minecraft.create('10.52.2.244')#
#mc = minecraft.Minecraft.create('10.52.3.39')#arse
#mc = minecraft.Minecraft.create('10.52.5.32')#
#mc = minecraft.Minecraft.create('10.52.3.11')#
#mc = minecraft.Minecraft.create('10.52.5.30')#
#cm = minecraft.Minecraft.create('10.52.5.124')#liam
mc = minecraft.Minecraft.create()#tobias
while True==True:
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    mc.setBlocks(x-1,y-1,z-1,x+1,y+1,z+1,0)
    if y <= -64:
        mc.player.setTilePos(x+2,44,z)
