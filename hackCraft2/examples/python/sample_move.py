from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

for i in range(5):
    hello.forward()
    hello.turnRight()

player.logout()
