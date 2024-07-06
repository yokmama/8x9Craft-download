from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

ret = hello.inspectDown()
hello.say(f"これは{ret.name}です。")

player.logout()
