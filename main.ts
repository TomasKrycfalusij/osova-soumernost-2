let displej = 5
let osaX = 2
let trojuhelnik = [[0, randint(0, displej - 1)], [1, randint(0, displej - 1)], [2, randint(0, displej - 1)]]
// OSA
function draw_osaX() {
    for (let i = 0; i < displej; i++) {
        led.plotBrightness(osaX, i, 100)
    }
}

// BODY
function klm() {
    for (let bod of trojuhelnik) {
        led.plot(bod[0], bod[1])
    }
}

// MIRROR
function mirror() {
    for (let bod of trojuhelnik) {
        led.plot(Math.abs(bod[0] - 4), bod[1])
    }
}

// ZABLIKANI
for (let a = 0; a < 3; a++) {
    draw_osaX()
    klm()
    mirror()
    basic.pause(1000)
    basic.clearScreen()
    draw_osaX()
    basic.pause(1000)
}
