from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

if(hello.isBlocked()):
    hello.dig()
    hello.forward()
    while True:
        if(not hello.digUp()):
            break
    hello.back()

player.logout()
