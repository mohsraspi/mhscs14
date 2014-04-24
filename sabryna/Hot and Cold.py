import minecraft as minecraft
import math
import time
import random
global tileX
global tileY

mc = minecraft.Minecraft.create()


##position = mc.player.getTilePos()
##
##x = position.x
##y = position.y
##z = position.z

tileX = random.randint(-127, 127)
tileZ = random.randint(-127, 127)
tileY = mc.getHeight(tileX, tileZ)
diamond = 57
block = diamond
mc.setBlock(tileX, tileY, tileZ, diamond)
print (tileX, tileY, tileZ)
##        mc.setBlock(1, 8, 21, diamond)
mc.postToChat('Block set')


while True == True:
        blockType = mc.getBlock(tileX, tileY, tileZ)
        if blockType == 0:
                mc.postToChat('You win!')
                time.sleep(5)
                tileX = random.randint(-127, 127)
                tileZ = random.randint(-127, 127)
                tileY = mc.getHeight(tileX, tileZ)
                diamond = 57
                block = diamond
                mc.setBlock(tileX, tileY, tileZ, diamond)
                print (tileX, tileY, tileZ)
                mc.postToChat('Block set')
               
        else:
                position = mc.player.getTilePos()
                x1 = position.x
                y1 = position.y
                z1 = position.z
                time.sleep(2)
                
                position = mc.player.getTilePos()
                x2 = position.x
                y2 = position.y
                z2 = position.z

                dist1x = abs(x1 - tileX)
                dist1y = abs(y1 - tileY)
                dist1z = abs(z1 - tileZ)

                dist2x = abs(x2 - tileX)
                dist2y = abs(y2 - tileY)
                dist2z = abs(z2 - tileZ)

                print (dist1x, dist1y, dist1z)
                print (dist2x, dist2y, dist2z)
                if dist2x > 3 and dist2z > 3:
                        if dist2x < dist1x and dist2z < dist1z:
                                mc.postToChat('Hotter')
                        if dist2x > dist1x and dist2z < dist1z:
                                mc.postToChat('Warmer')
                        if dist2x < dist1x and dist2z > dist1z:
                                mc.postToChat('Warmer')
                        if dist2x > dist1x and dist2z > dist1z:
                                mc.postToChat('Colder')

                        time.sleep(3)
                        
                elif dist2x < 3 and dist2z < 3:
                        mc.postToChat('YOU. ARE. ON. FIYAH!')
                        time.sleep(3)


                




                
##def temperature():
##        smallestDistance = 100
##        for tileX in crying:
##                if abs(tileX - x) > abs(tileY - y):
##                        distance = abs(tileX - x)
##                else:
##                        distance = abs(tileY - y)
##
##                if distance < smallestDistance:
##                        smallestDistance = distance
##        if smallestDistance == 0:
##                print("Now hit the block!")
##        else:
##                if smallestDistance < 20:
##                        print ("You're on fiyah!")
##                else:
##                        print (';_; No. Keep going!')




        
        
        
        
