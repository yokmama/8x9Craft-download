from dataclasses import dataclass
from py2hackCraft.modules import Player, Entity


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

hello.reset()
for i in range(10):
    hello.place()
    hello.back()

player.logout()
