from mcpi.minecraft import Minecraft
mc = Minecraft.create()

px, py, pz = mc.player.getTilePos()

def plantTree(x, y, z, leaf, tree):
    mc.setBlocks(x - 2, y + 4, z - 2, x + 2, y + 8, z + 2, leaf)
    mc.setBlocks(x, y, z, x, y + 5, z, tree)

for i in range(3):
    for j in range(3):
        for k in range(3):
            plantTree(px + i * j * k, py + i * j * k, pz + i * j * k, 46, 57)