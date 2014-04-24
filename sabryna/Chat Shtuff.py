name = raw_input("Username: ")

##while True == True:
##    boat = raw_input("Enter your message: ")
##    mc.postToChat(name + ": " + boat)

##x = int(raw_input("Giveth to me numbers: "))
##y = int(raw_input("Giveth to me numbers: "))
##z = int(raw_input("Giveth to me numbers: "))
##blockType = int(raw_input("Giveth to me numbers: "))
##
##mc.setBlock(x, y, z, blockType)

import minecraft as minecraft

mc = minecraft.Minecraft.create()

x1 = 6
y1 = 5
z1 = 22
x2 = 12
y2 = 10
z2 = 32

mc.setBlocks(x1, y1, z1, x2, y2, z2, 45)
mc.setBlocks(x1 + 1, y1 + 1, z1 + 1, x2 - 1, y2 - 1, z2 - 1, 0)

x = 7
y = 5
z = 31
blockType = 5


length = 5
width = 9

xcount = 0
zcount = 0

while xcount < length:
    while zcount < width:
        mc.setBlock(x + xcount, y, z - zcount, blockType)
        zcount = zcount + 1
    xcount = xcount + 1
    zcount = 0

x = 6
y = 6
z = 25
blockType = 0

mc.setBlock(x, y, z, blockType) 
y = y + 1
mc.setBlock(x, y, z, blockType)

mc.setBlock(x, y, z, 64)

x = 8
y = 7
z = 32

mc.setBlock(x, y, z, 20)

while True == True:
    x = x + 1
    blockType = 0
    mc.setBlock(x, y, z, blockType)

    if x < 11 and y < 9:
        x = 0
        y = y + 1
