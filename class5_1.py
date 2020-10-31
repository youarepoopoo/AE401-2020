from mcpi.minecraft import Minecraft

mc = Minecraft.create()

block = input("Please enter a block ID: ")
try:
    block = int(block)

    x, y, z, = mc.player.getTilePos()
    mc.setBlock(x, y, z, block)
except:
    print("Please enter a number")
finally:
    print("exit")