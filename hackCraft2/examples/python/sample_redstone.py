from py2hackCraft.modules import Player
import time

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

try:
    while True:
        hello.waitForRedstoneChange()    
        hello.up()
        hello.down()
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
