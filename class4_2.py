from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
while True:
    x, y, z, = mc.player.getTilePos()
    a = mc.getBlock(x + 1, y - 1, z)
    b = mc.getBlock(x - 1, y - 1, z)
    c = mc.getBlock(x, y - 1, z - 1)
    d = mc.getBlock(x, y - 1, z + 1)
    if a == 0 or b ==0 or c == 0 or d == 0:
        mc.setBlocks(x + 1, y - 1, z + 1, x - 1, y - 1, z - 1, 20)