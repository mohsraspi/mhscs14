import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
print("enter stuff")
x = float(input())
y = float(input())
z = float(input())

mc.player.setPos(x,y,z)
