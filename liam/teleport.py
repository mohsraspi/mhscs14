import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
print("enter stuff")
x = input()
y = input()
z = input()

mc.player.setTilePos(x,y,z)
