from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

x, y, z = mc.player.getTilePos()

while True:
    rx = random.randrange(-10, 10) + x
    rz = random.randrange(-10, 10) + z
    ry = random.randrange(20, 30) + y

    mc.spawnEntity(rx, ry, rz, 93)
    time.sleep(1)