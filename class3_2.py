from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

count = 0

while count < 10:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("Position:" + str(x) + "," + str(y) + "," + str(z))

    count = count +1
    time.sleep(1)