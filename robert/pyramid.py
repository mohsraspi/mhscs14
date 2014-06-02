import minecraft as minecraft
import time
mc=minecraft.Minecraft.create()
x=0
y=-42
z=0
mc.player.setTilePos(x,y,z)
time.sleep(5)
mc.setBlocks(-200,63,200,200,-63,-200,0)
mc.setBlocks(-200,-63,200,200,-63,-200,2)

mc.setBlocks(x+1,y,z+1,x-1,y,z-1,46,1)
mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,46,1)
mc.setBlocks(x+3,y-2,z+3,x-3,y-2,z-3,46,1)
mc.setBlocks(x+4,y-3,z+4,x-4,y-3,z-4,46,1)
mc.setBlocks(x+5,y-4,z+5,x-5,y-4,z-5,46,1)
mc.setBlocks(x+6,y-5,z+6,x-6,y-5,z-6,46,1)
mc.setBlocks(x+7,y-6,z+7,x-7,y-6,z-7,46,1)
mc.setBlocks(x+8,y-7,z+8,x-8,y-7,z-8,46,1)
mc.setBlocks(x+9,y-8,z+9,x-9,y-8,z-9,46,1)
mc.setBlocks(x+10,y-9,z+10,x-10,y-9,z-10,46,1)
mc.setBlocks(x+11,y-10,z+11,x-11,y-10,z-11,46,1)
mc.setBlocks(x+12,y-11,z+12,x-12,y-11,z-12,46,1)
mc.setBlocks(x+13,y-12,z+13,x-13,y-12,z-13,46,1)
mc.setBlocks(x+14,y-13,z+14,x-14,y-13,z-14,46,1)
mc.setBlocks(x+15,y-14,z+15,x-15,y-14,z-15,46,1)
mc.setBlocks(x+16,y-15,z+16,x-16,y-15,z-16,46,1)
mc.setBlocks(x+17,y-16,z+17,x-17,y-16,z-17,46,1)
mc.setBlocks(x+18,y-17,z+18,x-18,y-17,z-18,46,1)
mc.setBlocks(x+19,y-18,z+19,x-19,y-18,z-19,46,1)


