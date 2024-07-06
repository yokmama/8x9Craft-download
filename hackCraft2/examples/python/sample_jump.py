from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

for i in range(10):
    hello.addForce(0, 0.6, 0)
    hello.placeDown()

player.logout()
