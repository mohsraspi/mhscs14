import minecraft as minecraft
mc=minecraft.Minecraft.create()
players = mc.getPlayerEntityIds()
mc.postToChat(str(len(players)))
