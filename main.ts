let displej = 5
let osaX = 2
// OSA
function draw_osaX() {
    for (let i = 0; i < displej; i++) {
        led.plotBrightness(osaX, i, 100)
    }
}

// BODY
let A = []
function rozhod_body() {
    
    A = [2, randint(0, displej - 1)]
    let B = [randint(0, 1), randint(0, displej - 1)]
    let C = [randint(0, 1), randint(0, displej - 1)]
    if (B == C) {
        rozhod_body()
    }
    
}

rozhod_body()
console.log(A)
// def zobrazeni_bodu():
// led.plot(A[0], A[1])
for (let a = 0; a < 3; a++) {
    draw_osaX()
    // zobrazeni_bodu()
    basic.pause(1000)
    basic.clearScreen()
    basic.pause(1000)
}
