from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()
x,y,z, = mc.player.getTilePos()

mc.setBlocks(x + 3, y + 30, z + 3, x - 3, y + 30, z - 3, 20)
mc.player.setPos(x, y + 35, z)