from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

ret = hello.getLocation()
hello.forward()
hello.forward()
hello.teleport(ret)

player.logout()
