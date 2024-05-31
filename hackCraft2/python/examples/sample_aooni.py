from dataclasses import dataclass
from py2hackCraft.modules import Player, Entity
import time
import random

# 青鬼がもつアイテムの名前
event_item_name = "kill"

# 青鬼がプレイヤーを捕まえたときに転送する座標
respawn_pos = (91, 72, -13)

def onInteractEvent(entity, event):
    if( event.event == "kill"):
        if( event.type == "pet" or event.type == "player"):
            entity.executeCommand(f"entity here {event.name} {respawn_pos[0]} {respawn_pos[1]} {respawn_pos[2]}")

player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("hello")
test.setOnInteractEvent(onInteractEvent)


quit = input("Press Enter to quit...")
player.logout()
