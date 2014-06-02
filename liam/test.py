import bob.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
print(mc.player.getTilePos())

time.sleep(5)
L = mc.events.pollBlockHits()
print(L)
for h in L:
    print(h.pos)
    
