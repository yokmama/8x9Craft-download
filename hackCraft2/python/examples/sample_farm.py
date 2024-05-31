from py2hackCraft.modules import Player, Entity
from py2hackCraft.material import Items, Blocks

def plant(entity: Entity):
    block = entity.inspectDown()
    if block.name != Blocks.FARMLAND:
        entity.holdItem(0)
        entity.useItemDown()
    entity.holdItem(1)
    entity.useItemDown()


def farming(entity: Entity):
    block = entity.inspect()
    if block.name == Blocks.AIR:
        plant(entity)
    elif block.name == Blocks.WHEAT and block.data == 7:    
        entity.harvest()
        plant(entity)


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")
hello.setItem(0, Items.DIAMOND_HOE)
hello.setItem(1, Blocks.WHEAT_SEEDS)

home = hello.getLocation()
for x in range(5):
    hello.forward()
    farming(hello)
hello.teleport(home)    

player.logout()


