import minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        print str(hit.pos.x) + ", " + str(hit.pos.x) + ", " + str(hit.pos.y) + ", " + str(hit.pos.z)
             
        time.sleep(0.1)
                                            
