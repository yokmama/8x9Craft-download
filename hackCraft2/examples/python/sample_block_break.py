from py2hackCraft.modules import Player
import time

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

try:
    while True:
        block = hello.waitForBreakBlock()    
        print("example::onBlockBreak %s %d %d %d" %(block.name, block.x, block.y, block.z))
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
