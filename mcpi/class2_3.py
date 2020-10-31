from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

x = 100
y = 70
z = 100

time.sleep(1)
mc.player.setTilePos(x,y,z)

y = y + 10
time.sleep(1)
mc.player.setTilePos(x,y,z)

y = y + 10
time.sleep(1)
mc.player.setTilePos(x,y,z)