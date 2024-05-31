from py2hackCraft.modules import Player
import time
import google.generativeai as genai

genai.configure(api_key='<API KEY>')

model = genai.GenerativeModel('gemini-pro')

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")
try:
    while True:
        hello.say("なにか手伝えることはありますか？")
        chat = hello.waitForPlayerChat()
        response = model.generate_content(f"これ「${chat.message}」を牛の言葉で返事してください。")
        hello.say(response.text)
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
