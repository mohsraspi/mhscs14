import bob.minecraft as minecraft
mc = minecraft.Minecraft.create("10.52.4.16")
Dict = {2:13,1:7,8:11,9:11,3:12,12:4,24:4,13:8,7:15,78:16,80:16,79:3,18:5,17:1}
for x in range(-130,130):
    for z in range(-130,130):
        for y in range((-1,(mc.getHeight(x,z))):
            w = mc.getBlock(x,y,z)
            if w in Dict:
                mc.setBlock(x,y,z,35,Dict[w])
print("done")
            

