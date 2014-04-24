    import minecraft as minecraft
import time
import random

inventory = []

mc = minecraft.Minecraft.create()

players = mc.getPlayerEntityIds()
inventory.append(players)

mc.postToChat(str(len(players)))

print (inventory)

playerId = 319

for key in inventory:
    while True == True:
        print (key)
        mc.camera.setFollow(playerId)
        time.sleep(4)

