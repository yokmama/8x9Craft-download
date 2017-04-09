crab.setHome("s")
var data = eval(crab.readFile("data"))
var width = data[0].length
var height = data.length

for(var i=height-1; i>=0; i--){
    for(var j=0; j<width; j++){
        var color = data[i][j]
        var meta
        switch(color){
            case 0: meta = 5; break
            case 1: meta = 15; break
        }
        crab.place("wool", meta)
        crab.stepRight()
    }
    crab.home("s")
    crab.turnRight()
    crab.up()
    crab.setHome("s")
}