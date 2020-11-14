from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
for k in range(10):
    for j in range(10):
        for i in range(10):
            mc.setBlock(x + i, y + k, z + j, 46)