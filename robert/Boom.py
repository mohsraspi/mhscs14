import minecraft as minecraft
import block as block
import time
import threading
fuseInSecs = 2
mc = 2
class ExplodingBlock(threading.Thread):
    def __init__(self, pos,fuseInSecs, blastRadius):
        threading.Thread.__init__(self)
        self.pos = pos
        self.fuseInSecs = fuseInSecs
        self.blastRadius = blastRadius

    def run(self):
        mc = minecraft.Minecraft.create()
        pos = self.pos
        blastRadius = self.blastRadius
        blockType = mc.getBlock(pos.x, pos.y, pos.z)
    for fuse in range(0, fuseInSecs):
        mc.setBlock(pos.x,pos.y,pos.z,0)
        time.sleep(0.5)
        mc.setBlock(pos.x,pos.y,pos.z, blockType)
        time.sleep(0.5)
    for x in range(blastRadius*-1,blastRadius):
        for y in range(blastRadius*-1,blastRadius):
            for z in range(blastRadius*-1,blastRadius):
                if x**2 + y**2 + z**2 <blastRadius**2:
                    mc.setBlock(int(pos.x + x), int(pos.y + y), int(pos.z + z), 0)
if __name__ == "__main__":
    time.sleep(5)
    mc = mc.minecraft.create()
    mc.postToChat("Minecraft Bombs, Hit (Right Click) a Block.")
    if blockHits:
        for blockHit in blockHits:
            explodingBlock = ExplodingBlock(blockHit.pos, 3, 3)
            explodingBlock.daemon
            explodingBlock.start()
        time.sleep(0.1)
    
