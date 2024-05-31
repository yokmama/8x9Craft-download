from py2hackCraft.modules import Player, Entity

def selectionSort(entity: Entity):
    n = 9
    # 配列の各要素に対して
    for i in range(n):
        # 最小要素のインデックスを探す
        min_index = i
        for j in range(i+1, n):
            if entity.getItem(min_index).amount > entity.getItem(j).amount:
                min_index = j
        
        # 最小要素を未ソート部分の最初の要素と交換
        entity.swapItem(i, min_index)

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.getEntity("hello")

selectionSort(hello)

player.logout()
