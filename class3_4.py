from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z, = mc.player.getTilePos()

mc.setBlocks(x, y, z, x + 3, y + 3, z + 3, 46)