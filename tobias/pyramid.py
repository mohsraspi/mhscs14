import minecraft as minecraft
mc = minecraft.Minecraft.create()
p=25
y=-5
n=-25
while p >= 1:
    mc.setBlocks(p,y,p,n,y,n,45)
    p = p-1
    n = n+1
    y = y+1
