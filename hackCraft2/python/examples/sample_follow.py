from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

while True:
    hello.lookAtTarget(player.uuid)
    hello.addForce(0, 0, 0.3)