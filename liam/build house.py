import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

##position = mc.player.getTilePos()
##x= position.x
##y= position.y
##z= position.z



def makeFloor():
    for y in [-20,-10,0,10,20,30,40,50,60]:
        mc.setBlocks(-20,y,-20,20,y,20,17,1)
        mc.setBlocks(-19,y,-19,19,y,19,5)
def makeS():
    mc.setBlocks(-20,-20,-20,20,60,-20,20)
    mc.setBlocks(-20,-20,-20,-20,60,20,20)
    mc.setBlocks(20,-20,-20,20,60,20,20)
    mc.setBlocks(-20,-20,-20,20,60,20,20)
    for x in [-20,-7,7,20]:
        for z in [-20,-7,7,20]:
            mc.setBlocks(x,-20,z,x,60,z,17,1)
            
   
def makeD():
    for y in [-20,-10,0,10,20,30,40,50,60]:
        mc.setBlocks(-20,y+1,-2,-20,y+5,2,0)
        mc.setBlocks(20,y+1,-2,20,y+5,2,0)
        mc.setBlocks(-2,y+1,-20,2,y+5,-20,0)
        mc.setBlocks(-2,y+1,20,2,y+5,20,0)
        mc.setBlocks(-20,y+1,-2,-20,y+1,2,85)
        mc.setBlocks(20,y+1,-2,20,y+1,2,85)
        mc.setBlocks(-2,y+1,-20,2,y+1,-20,85)
        mc.setBlocks(-2,y+1,20,2,y+1,20,85)
        mc.setBlock(-20,y+1,0,107,1)
        mc.setBlock(20,y+1,0,107,1)
        mc.setBlock(0,y+1,-20,107)
        mc.setBlock(0,y+1,20,107)
def pool():
    mc.setBlocks(-12,47,-12,12,50,12,17)
    mc.setBlocks(-11,48,-11,11,50,11,8)
def Lad():
    mc.setBlocks(-7,-19,-19,-7,60,-19,65,3)
    mc.setBlocks(7,-19,-19,7,60,-19,65,3)
    mc.setBlocks(-7,-19,19,-7,60,19,65,2)
    mc.setBlocks(7,-19,19,7,60,19,65,2)
    mc.setBlocks(-19,-19,-7,-19,60,-7,65,5)
    mc.setBlocks(19,-19,-7,19,60,-7,65,4)
    mc.setBlocks(-19,-19,7,-19,60,7,65,5)
    mc.setBlocks(19,-19,7,19,60,7,65,4)


def Kit():
    mc.setBlocks(-12,46,-12,12,46,12,17,1)
    mc.setBlocks(-11,46,-11,11,46,11,0)
    for x in [-10,-8,-6,-4,-2,0,2,4,6,8,10]:
        for z in [-10,-8,-6,-4,-2,0,2,4,6,8,10]:
            mc.setBlock(x,46,z,17,1)
    for x in [-11,-9,-7,-5,-3,-1,1,3,5,7,9,11]:
        for z in [-11,-9,-7,-5,-3,-1,1,3,5,7,9,11]:
            mc.setBlock(x,46,z,89)
    mc.setBlocks(-12,41,-12,12,41,12,1)
    mc.setBlocks(-12,42,-12,12,42,12,44)
    mc.setBlocks(-11,41,-11,11,42,11,0)
    mc.setBlocks(-11,41,-11,0,41,0,1)
    mc.setBlocks(-11,42,-11,0,42,0,44)
    mc.setBlocks(-11,41,-11,-1,42,-1,0)
    mc.setBlocks(-6,41,0,-6,42,0,0)
    mc.setBlocks(12,41,-1,12,42,1,0)
    mc.setBlocks(-8,41,2,-8,41,10,109)
    mc.setBlocks(-10,41,2,-10,41,10,109,1)
    mc.setBlocks(-9,41,2,-9,41,10,85)
    mc.setBlocks(-9,42,2,-9,42,10,44,2)
    mc.setBlocks(-4,41,10,9,41,10,109,2)
    mc.setBlocks(-4,41,8,9,41,8,109,3)
    mc.setBlocks(-4,41,9,9,41,9,85)
    mc.setBlocks(-4,42,9,9,42,9,44,2)
    mc.setBlocks(-4,41,5,9,41,5,109,2)
    mc.setBlocks(-4,41,3,9,41,3,109,3)
    mc.setBlocks(-4,41,4,9,41,4,85)
    mc.setBlocks(-4,42,4,9,42,4,44,2)
    mc.setBlocks(7,41,-9,7,41,-3,109,1)
    mc.setBlocks(10,41,-9,10,41,-3,109)
    mc.setBlocks(9,41,-9,8,41,-3,85)
    mc.setBlocks(9,42,-9,8,42,-3,44,2)
    mc.setBlocks(2,41,-9,2,41,-3,109,1)
    mc.setBlocks(5,41,-9,5,41,-3,109)
    mc.setBlocks(3,41,-9,4,41,-3,85)
    mc.setBlocks(3,42,-9,4,42,-3,44,2)
    mc.setBlocks(-11,41,-11,-11,41,-1,62)
    mc.setBlocks(-1,41,-11,-1,41,-1,24,2)
    mc.setBlocks(-9,41,-11,-3,41,-11,54)
    
def Torch():
    for y in [-20,-10,0,10,20,30,40,50]:
        mc.setBlock(-3,y+5,-19,50,5)
        mc.setBlock(3,y+5,-19,50,5)
        mc.setBlock(-3,y+5,19,50,5)
        mc.setBlock(3,y+5,19,50,5)
        
    

























    

##mc.setBlocks(-20,-20,-20,20,60,20,5)
##makeS()
##mc.setBlocks(-19,-19,-19,19,59,19,0)
##makeFloor()
##mc.setBlocks(-19,60,-19,19,60,19,20)
##mc.setBlocks(-20,61,-20,20,61,20,85)
##mc.setBlocks(-19,61,-19,19,61,19,0)
##makeD()
##pool()
##Lad()
##Kit()
Torch()
