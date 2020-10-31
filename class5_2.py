from mcpi.minecraft import Minecraft
mc = Minecraft.create()

user = input("Enter your name ")
while True:
    message = input("Enter a message ")

    mc.postToChat("<" + user + ">" + message)