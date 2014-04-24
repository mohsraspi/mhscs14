import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time
if __name__ == "__main__":
 
 
# - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()
 
#Post a message to the minecraft chat window
    mc.postToChat("Aura Of Destruction activated")
 
    try:
        while True:
            playerPos = mc.player.getPos()
            playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
            #to resolve issues with negative positions
            if playerPos.z < 0:
                playerPos.z = playerPos.z - 1
            if playerPos.x < 0:
                playerPos.x = playerPos.x - 1
            if playerPos.y < 0:
                playerPos.y = playerPos.y - 1
            mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.AIR)
            mc.setBlock(playerPos.x,playerPos.y,playerPos.z+1,block.AIR)
            mc.setBlock(playerPos.x,playerPos.y,playerPos.z-1,block.AIR)
            mc.setBlock(playerPos.x,playerPos.y+1,playerPos.z+1,block.AIR)
            mc.setBlock(playerPos.x,playerPos.y+1,playerPos.z-1,block.AIR)
            mc.setBlock(playerPos.x+1,playerPos.y,playerPos.z,block.AIR)
            mc.setBlock(playerPos.x-1,playerPos.y,playerPos.z,block.AIR)
            mc.setBlock(playerPos.x+1,playerPos.y+1,playerPos.z,block.AIR)
            mc.setBlock(playerPos.x-1,playerPos.y+1,playerPos.z,block.AIR)
    except KeyboardInterrupt:
            time.sleep(1)
