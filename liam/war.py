import bob.minecraft as minecraft
mc1 = minecraft.Minecraft.create()
mc2 = minecraft.Minecraft.create("10.52.2.248")
e = 6
L1 = mc1.getPlayerEntityIds()
f1 =[]
f2 =[]
L2 = mc2.getPlayerEntityIds()
for i in L1:
    mc1.entity.setTilePos(i,0,20,0)
for i in L2:
    mc2.entity.setTilePos(i,0,20,0)
while e == 6:
    for i in L1:
    
        
        position = mc1.entity.getTilePos(i)
        x= position.x
        y= position.y
        z= position.z
        mc2.setBlock(x,y,z,35,14)
        f1.append([x,y,z])
        
    for i in L2:
        
        position = mc2.entity.getTilePos(i)
        x= position.x
        y= position.y
        z= position.z
        mc1.setBlock(x,y,z,35,14)
        f2.append([x,y,z])
        
    for w in range(len(f1)):
        x = f1[w][0]
        y = f1[w][1]
        z = f1[w][2]
        for h in mc2.events.pollBlockHits():
            X = h.pos.x
            Y = h.pos.y
            Z = h.pos.z
            if x == X and y == Y and z == Z:
                print("hi")
                mc1.entity.setTilePos(L1[w],0,20,0)
        
    for w in range(len(f2)):
        
        x = f2[w][0]
        y = f2[w][1]
        z = f2[w][2]
        for h in mc1.events.pollBlockHits():
            X = h.pos.x
            Y = h.pos.y
            Z = h.pos.z
            if x == X and y == Y and z == Z:
                print("hi")
                mc2.entity.setTilePos(L2[w],0,20,0)
        
    for w in range(len(f1)):
        x = f1[w][0]
        y = f1[w][1]
        z = f1[w][2]
        mc2.setBlock(x,y,z,0)
    for w in range(len(f2)):
        x = f2[w][0]
        y = f2[w][1]
        z = f2[w][2]
        mc1.setBlock(x,y,z,0)
    f1 = []
    f2 = []   
        
