import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
z = 10
while z == 10:
    x = str(input())
    mc.postToChat(x)
