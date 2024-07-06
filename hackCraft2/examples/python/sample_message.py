from py2hackCraft.modules import Player
import time

def onMessage(entity, event):
    print("Message from %s: %s" % (event.sender, event.message))
    entity.say("I got your message!")

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

hello.setOnMessage(onMessage)

hello.sendMessage("hello", "hello")   

quit = input("Press Enter to quit...")
player.logout()
