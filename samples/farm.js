function tanemaki(){
    crab.useDown()
    crab.placeDown("wheat_seeds", 0)
}

for(let i=0; i<2; i++){
    for(let j=0; j<5; j++){
        var item = crab.inspectDown()
        if(item.id == 0){ //空気だったら
            tanemaki()
        }else if(item.meta == 7){ //刈り入れできるなら
            crab.digDown()
            tanemaki()                        
        }
        crab.forward()
    }
    crab.turnLeft()
    crab.forward()
    crab.turnLeft()
    crab.forward()
}
