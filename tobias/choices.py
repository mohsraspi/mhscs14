import minecraft as minecraft
import time
#This program was made by Tobias Kipps
print('Enter IP')
ipo=input()
mc=minecraft.Minecraft.create(ipo)
mc.setBlocks(-5,-5,-5,5,5,5,45)
mc.setBlock(0,5,0,89)
mc.setBlocks(-4,-4,-4,4,4,4,0)
mc.setBlock(2,-4,-3,41)
mc.setBlock(2,-4,3,41)
mc.setBlocks(50,50,50,52,52,-50,103)
mc.setBlocks(51,51,49,51,51,-49,46,1)
pg=1
mc.postToChat('go left')
mc.player.setTilePos(0,0,0)
while pg==1:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=2
        mc.postToChat('Thank you')
        mc.postToChat('Now go right')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=3
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Please go left')
    
while pg==2:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=4
        mc.postToChat('What')
        mc.postToChat('No. Go right.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=5
        mc.player.setTilePos(0,0,0)
        mc.postToChat('You are doing very well.')
        mc.postToChat('Go right again')
while pg==3:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=6
        mc.postToChat('Thank you.')
        mc.postToChat('Now go right')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=7
        mc.player.setTilePos(0,0,0)
        mc.postToChat('No! That is the wrong way!')
        mc.postToChat('This is your last chance. Go left.')
while pg==4:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=8
        mc.postToChat('I am getting fed up with this.')
        mc.postToChat('Go right. I will not give you any more chances.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=9
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Excelent.')
        mc.postToChat('Now go forward.')
        mc.setBlocks(-5,-5,-5,5,5,55,45)
        mc.setBlock(0,5,0,89)
        mc.setBlocks(-4,-4,-4,4,4,54,0)
        mc.setBlock(0,-4,52,41)
while pg==5:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=10
        mc.postToChat('What')
        mc.postToChat('No. Go right.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=11
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Perfect! You are doing great.')
        mc.postToChat('Now go left OR right.')
        mc.setBlock(2,-4,0,41)
while pg==6:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=12
        mc.postToChat('What')
        mc.postToChat('No. Go right.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=13
        mc.player.setTilePos(0,0,0)
        mc.postToChat('You are doing very well.')
        mc.postToChat('Go right again')
while pg==7:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=14
        mc.postToChat('Finally')
        mc.postToChat('Now you can go right.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=15
        mc.player.setTilePos(0,0,0)
        mc.postToChat('I warned you!')
        mc.setBlocks(-4,-4,-4,4,4,4,10)
        time.sleep(7)
        mc.player.setTilePos(-667,-646,-667)
while pg==8:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=16
        mc.player.setTilePos(0,0,0)
        mc.postToChat('I warned you!')
        mc.setBlocks(-4,-4,-4,4,4,4,10)
        time.sleep(7)
        mc.player.setTilePos(-667,-646,-667)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=17
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Alright, good.')
        mc.postToChat('Now go right again')
while pg==9:
    if mc.player.getTilePos().x==0 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==52:
        pg=18
        mc.postToChat('Well, I am getting bored of this.')
        mc.postToChat('I guess ill just say you win. Yay.')
        mc.setBlock(0,-4,52,46,1)
        mc.setBlocks(-5,-6,-5,5,-6,55,46,1)
while pg==10:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=19
        mc.postToChat('Seriously, go right.')
        mc.postToChat('My patince is running out.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=20
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Good.')
        mc.postToChat('Now go right again')

while pg==11:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=21
        mc.postToChat('Very good!')
        mc.postToChat('You win!')
        time.sleep(3.5)
        mc.player.setTilePos(0,6,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=22
        mc.postToChat('Congradulations!')
        mc.postToChat('You win!')
        time.sleep(3.5)
        mc.player.setTilePos(0,6,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==0:
        pg=23
        mc.postToChat('No! Not that one!')
        mc.postToChat('Only left or right.')
        mc.player.setTilePos(0,0,0)
while pg==12:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=24
        mc.postToChat('This is your last chance.')
        mc.postToChat('Go right.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.playerr.getTilePos().z==3:
        pg=25
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Good.')
        mc.postToChat('Now go right again')
while pg==13:
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==-3:
        pg=26
        mc.postToChat('What')
        mc.postToChat('No. Go right.')
        mc.player.setTilePos(0,0,0)
    if mc.player.getTilePos().x==2 and mc.player.getTilePos().y==-3 and mc.player.getTilePos().z==3:
        pg=27
        mc.player.setTilePos(0,0,0)
        mc.postToChat('Yay!')
        mc.postToChat('You win.')
        time.sleep(1.8)
        mc.setBlocks(7,7,7,7,7,7,7)
