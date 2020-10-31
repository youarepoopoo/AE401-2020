from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z, = mc.player.getTilePos()

w = 10
h = 8
l = 20

mc.setBlocks(x, y, z, x + w, y + h, z + l, 0)
mc.setBlocks(x + 2, y + 2, z + 2, x + w - 2, y + h - 2, z + l - 2, 0)