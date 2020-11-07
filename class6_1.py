from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z, = hit.pos
        block = mc.getBlock(x, y, z)
        if block == 1:
            mc.setBlocks(x, y, z, x + 3, y, z + 3, 46)