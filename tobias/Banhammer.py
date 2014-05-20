import minecraft as minecraft
#mc = minecraft.Minecraft.create('10.52.3.80')
#mc = minecraft.Minecraft.create('10.52.4.54')#jay
#mc = minecraft.Minecraft.create('10.52.3.139')
#mc = minecraft.Minecraft.create('10.52.3.39')#asshole
#mc = minecraft.Minecraft.create('10.52.3.235')#steven
#mc = minecraft.Minecraft.create('10.52.2.244')
#mc = minecraft.Minecraft.create()#tobias
iplol=input()
mc = minecraft.Minecraft.create(iplol)#tobias
while True==True:
    x=mc.player.getTilePos().x
    y=mc.player.getTilePos().y
    z=mc.player.getTilePos().z
    mc.player.setTilePos(x,y+1,z)
