from py2hackCraft.modules import Player, Coordinates
from PIL import Image

# 画像ファイルを開く
file = Image.open('creeper.png')

# 画像をRGBモードに変換
image = file.convert('RGB')


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

for y in range(image.height):
    for x in range(image.width):
        # 指定位置のピクセルのRGB値を取得
        rgb = image.getpixel((x, y))
        hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        block = hello.getBlockByColor(hex_color)
        hello.setBlock(Coordinates.local, x, image.height-y + 1, 1, block.name)
